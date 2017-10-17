# encoding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import gzip
import unicodedata
import argparse
import re
import string
import intertools
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

def safeopen(file):
    from os import makedirs
    from os.path import dirname
    makedirs(dirname(file), exist_ok=True)
    return open(file,'w') 
def randomRack(tiles,n=MAX_RACK):
    tiles_list = list(''.join(letter*tiles[letter][REP] for letter in tiles.keys()))
    np.random.shuffle(tiles_list)
    print(tiles_list[:n])

### ARGUMENT PARSER SETUP ###
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-s', '--stadistics',help='TO DO', action='store_true')
group.add_argument('-n',help='TO DO', type=int)
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
parser.add_argument('-o','--output',help='escribe la salida en un archivo dado')
# args = parser.parse_args(['-r','cosaoa','-m','.o.a']) #Test!
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
    validwords = []
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


### OUTPUT PREPARATION ###
s = 'Resultado:'
if args.rack is not None:
    if len(validwords) == 0:
        s+='\nNo se encontraron palabras!'
    else:
        for (score,word) in validwords:
            s+='\n{} puntos: {}'.format(score,replaceSpecial(word,reverse=True))
else:
    if args.stadistics:
        hist = { score : frecuency for }
    else:
        for rack, (score, word) in output.items():
            if len(validwords) == 0:
                s+='\nrack: {!r}, no se encontraron palabras'.format(rack)
            else:
                s+='\nrack: {!r}, puntos: {}, palabra: {!r}'.format(rack,score,replaceSpecial(word,reverse=True))

### PRINT OUTPUT ###
if args.output is None:
    print(s)
else:
    with safeopen(args.output) as file:
        if args.output.endswith('.png'):
            raise NotImplementedError
        else:
            file.write(s)