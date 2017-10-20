# encoding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import gzip
import unicodedata
import argparse
import re
import string

### CONSTANTS ###
RR = '0'
CH = '1'
LL = '2'
BLANK = '#'

REP = 0
VAL = 1

ENGLISH = 'en'
SPANISH = 'es'

DEFAULT_MODEL = '.'

PATH_ES = 'palabras.words.gz'
PATH_EN = 'palabras_en.words.gz'

MAX_RACK = 7
MAX_OUTPUT = 5

EMPTY = ''
EMPTY_SCORE = 0

MODEL_LIST = string.ascii_lowercase+'\A'+'\Z'+'.'+RR+CH+LL

### HELPERS ###
def replaceSpecial(word, reverse=False):
    mapa = [('rr',RR),('ch',CH),('ll',LL)]
    old = int(reverse)
    new = int(not reverse)
    for pair in mapa:
        if pair[old] in word:
            word = word.replace(pair[old],pair[new])
    return word

### ARGUMENT PARSER SETUP ###
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-n',help='ingrese el numero de veces que quiere sortear rack', type=int)
group.add_argument('-r','--rack', 
    help="""ingrese las letras que le tocaron. 
            RR se ingresa como {!r}, 
            CH como {!r}, 

            LL como {!r} 
            y el comodin como {!r}""".format(RR,CH,LL,BLANK))
parser.add_argument('-m','--model',default=DEFAULT_MODEL,
    help="""ingrese un patron que quiera que las palabras cumplan.
            'A...Z' para indicar  letras presentes en el tablero.
            '.' para forzar la colocacion de una de sus fichas.
            '\A' y '\Z' para indicar el inicio o fin del tablero.
            Ejemplo: .a.o\Z -> abaco""")
parser.add_argument('-l', '--language', help="elija el lenguaje entre {!r} (default) y {!r}".format(SPANISH,ENGLISH), choices=[SPANISH,ENGLISH], default=SPANISH)
parser.add_argument('-s', '--stadistics',help='realiza un histograma del resultado del argumento -n. si -o termina en .png se genera una figura', action='store_true')
parser.add_argument('-o','--output',help='escribe la salida en un archivo dado')
args = parser.parse_args()

### LANGUAGE SETUP ###
if args.language == SPANISH:
    fileName = PATH_ES
    tiles = {RR: (1, 8),CH: (1,5), LL: (1, 8), 'u': (5, 1), 'o': (9, 1), 'v': (1, 4), 'ñ': (1, 8), 'q': (1, 5), 'g': (2, 2), 'e': (12, 1), 'd': (5, 2), 'y': (1, 4), 'b': (2, 3), 'h': (2, 4), 'p': (2, 3), 'c': (4, 3), 'n': (5, 1), 'x': (1, 8), 'a': (12, 1), 'r': (5, 1), BLANK: (2, 0), 's': (6, 1), 'l': (4, 1), 'j': (1, 8), 'z': (1, 10), 'f': (1, 4), 't': (4, 1), 'i': (6, 1), 'm': (2, 3)}
elif args.language == ENGLISH:
    fileName = PATH_EN
    tiles = {'u': (4, 1), 'o': (8, 1), 'k': (1, 5), 'v': (2, 4), 'q': (1, 10), 'l': (4, 1), 'g': (3, 2), 'e': (12, 1), 'd': (4, 2), 'y': (2, 4), 'b': (2, 3), 'h': (2, 4), 'p': (2, 3), 'c': (2, 3), 'n': (6, 1), 'x': (1, 8), 'a': (9, 1), 'r': (6, 1), BLANK: (2, 0), 's': (4, 1), 'w': (2, 4), 'j': (1, 8), 'z': (1, 10), 'f': (2, 4), 't': (6, 1), 'i': (9, 1), 'm': (2, 3)}

### CHECK MODEL INPUT ###
board = ''
for letter in args.model.replace('\A','').replace('\Z','').lower():
    if letter in MODEL_LIST:
        if letter in tiles.keys():
            board += letter
    else:
        print('El caracter {!r} en el modelo, no esta permitido'.format(letter))
        exit(1)
pattern = re.compile(args.model)
    
### POPULATE RACKLIST ###
racklist = []
if args.rack is not None:
    ### CHECK RACK INPUT ###
    for letter in args.rack.lower():
        if letter in tiles.keys():
            if args.rack.count(letter) > tiles[letter][REP]:
                print('No hay suficientes fichas de la letra:', letter)
                exit(1)
        else:
            print('El caracter {!r} no participa del juego'.format(letter))
            exit(1)
    racklist.append(args.rack.lower())
else:
    ### POPULATE RANDOM RACKS ###
    tiles_list = list(''.join(letter*tiles[letter][REP] for letter in tiles.keys()))
    for i in range(args.n):
        np.random.shuffle(tiles_list)
        racklist.append(''.join(tiles_list[:MAX_RACK]))

### TRY LOAD WORDLIST ###
wordlist = []
try:
    with gzip.open(fileName,'rt',encoding='utf-8') as file:
        for line in file:
            if line.islower():
                word = unicodedata.normalize('NFKD', line.strip()).encode('ASCII', 'ignore').decode('utf-8')
                wordlist.append(replaceSpecial(word))
except FileNotFoundError:
    print('No se encuentra el archivo: {!r}'.format(fileName))
    exit(1)

### CHECK EVERY WORD IN WORDLIST FOR EVERY RACK ###
output = {}
for rack in racklist:
    validwords = [(EMPTY_SCORE,EMPTY)]
    for word in wordlist:
        isCandidate = True
        rack_letters = list(rack)
        board_letters = list(board)
        total = 0

        for letter in word:
            if letter in board_letters:
                board_letters.remove(letter)
            elif letter in rack_letters:
                rack_letters.remove(letter)
                total += tiles[letter][VAL]
            elif BLANK in rack_letters:
                rack_letters.remove(BLANK)
                total += tiles[BLANK][VAL]
            else:
                isCandidate = False
                break # pasa a la siguiente palabra

        if isCandidate:
            if pattern.search(word) is not None:
                validwords.append((total,word))
                
    validwords.sort(reverse=True)
    output[rack] = validwords[0]


### OUTPUT POST-PROCESSING ###
s = 'Resultado:'
if args.rack is not None:
    if len(validwords) == 1:
        s+='\nNo se encontraron palabras!'
    else:
        for (score,word) in validwords[0:MAX_OUTPUT]:
            s+='\n{} puntos: {}'.format(score,replaceSpecial(word,reverse=True))
else:
    if args.stadistics:
        data = [score for score, word in output.values()]
        scores = range(max(data)+1)
        frecuency=[]
        for i in scores:
            frecuency.append(data.count(i))
        for score, frec in zip(scores,frecuency):
            s+='\n{} puntos: {} veces'.format(score,frec)
    else:
        for rack, (score, word) in output.items():
            s+='\nrack: {!r}, puntos: {}, palabra: {!r}'.format(rack,score,replaceSpecial(word,reverse=True))

### OUTPUT PRINTING ###
if args.output is None:
    print(s)
else:
    if args.output.endswith('.png'):
        plt.bar(scores,frecuency)
        plt.xticks(scores)
        plt.xlabel('Puntaje')
        plt.ylabel('Frecuencia')
        plt.title('Histograma de palabras de maximo\n puntaje para {} racks elegidos al azar'.format(args.n))
        plt.savefig(args.output)
    else:
        with open(args.output,'w') as file:
            file.write(s)