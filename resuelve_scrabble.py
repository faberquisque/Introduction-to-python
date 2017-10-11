# encoding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import gzip
import unicodedata
import argparse
def translate(word, reverse=False):
    mapa = [('rr','0'),('ch','1'),('ll','2')]
    old = int(reverse)
    new = int(not reverse)
    for pair in mapa:
        if pair[old] in word:
            word = word.replace(pair[old],pair[new])
    return word

language = 'es'
rack = 'ved'
parser = argparse.ArgumentParser()
# parser.add_argument('rack',help="ingrese las letras que le tocaron. RR se ingresa como '0', CH como '1', LL como '2' y el comodin como '#'")
parser.add_argument('-l', '--language', help="elija el lenguaje entre 'es' y 'en'", choices=['es','en'])
parser.add_argument('-n',help='')
parser.add_argument('-o','-output',help='escribe la salida en un archivo dado')
args = parser.parse_args()

if language == 'es':
    fileName = 'palabras.words.gz'
    tiles = {'0': (1, 8), '2': (1, 8), 'u': (5, 1), 'o': (9, 1), 'v': (1, 4), 'ñ': (1, 8), 'q': (1, 5), 'g': (2, 2), 'e': (12, 1), 'd': (5, 2), 'y': (1, 4), 'b': (2, 3), 'h': (2, 4), 'p': (2, 3), 'c': (4, 3), 'n': (5, 1), 'x': (1, 8), 'a': (12, 1), 'r': (5, 1), '#': (2, 0), 's': (6, 1), 'l': (4, 1), '1': (1, 5), 'j': (1, 8), 'z': (1, 10), 'f': (1, 4), 't': (4, 1), 'i': (6, 1), 'm': (2, 3)}
elif language == 'en':
    fileName = 'palabras_en.words.gz'
    tiles = {'u': (4, 1), 'o': (8, 1), 'k': (1, 5), 'v': (2, 4), 'q': (1, 10), 'l': (4, 1), 'g': (3, 2), 'e': (12, 1), 'd': (4, 2), 'y': (2, 4), 'b': (2, 3), 'h': (2, 4), 'p': (2, 3), 'c': (2, 3), 'n': (6, 1), 'x': (1, 8), 'a': (9, 1), 'r': (6, 1), '#': (2, 0), 's': (4, 1), 'w': (2, 4), 'j': (1, 8), 'z': (1, 10), 'f': (2, 4), 't': (6, 1), 'i': (9, 1), 'm': (2, 3)}
else:
    print('Idioma no soportado. Elija entre (es) y (en)')
    exit(1)

wordlist = []
try:
    with gzip.open(fileName,'rt',encoding='utf-8') as file:
        for line in file:
            if line.islower():
                word = unicodedata.normalize('NFKD', line.strip()).encode('ASCII', 'ignore').decode('utf-8')
                
                wordlist.append(translate(word))
except EnvironmentError:
    print('No se encuentra el archivo:',fileName)
    exit(1)

for letter in rack:
    if k, (rep,val) in tiles.items():
        if rep > 0:
            tiles[k] = (rep-1,val)
        else:
            print('No hay suficientes fichas de la letra:', letter)
            exit(1)
    else:
        print('El caracter',letter,'no participa del juego')

validwords = []
for word in wordlist:
    isCandidate = True
    rack_letters = list(rack)

    for letter in word:
        if letter in rack_letters:
            rack_letters.remove(letter)
        else:
            isCandidate = False
            break
            
    if isCandidate:
        total = 0
        for letter in word:
            total += tiles[letter][1]
        validwords.append((total,word))

validwords.sort(reverse=True)
for (score,word) in validwords[0:5]:
    print('{}:\t{} puntos'.format(translate(word,reverse=True),score))