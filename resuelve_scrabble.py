# encoding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import gzip
import unicodedata

class Tile():
    def __init__(self,letter, repetition, value):
        self.letter = letter
        self.repetition = repetition
        self.value = value

    def RemoveOne(self):
        if self.repetition > 0:
            self.repetition-=1
        else:
            raise NameError('Execedio la cantidad de fichas de la letra: {}'.format(self.letter))

    def AddOne(self):
        self.repetition+=1

    def __str__(self):
        return '{}: r={} v={}'.format(self.letter,self.repetition,self.value)

class Word():
    def __init__(self, string, alphabet):
        self.tiles = {}
        for char in string:
            if char.isalpha()
                if char in self.tiles.keys():
                    self.tiles[char].AddOne()
                else:
                    self.tiles[char] = Tile(char,1,alphabet[char])
    def AddTile(tile):
        if tile.letter in self.tiles.keys():
            self.tiles[tile.letter].AddOne()
        else:
            self.tiles[tile.letter] = Tile(tile.letter,1,alphabet[char])

    def sum(self):
        return sum([k.repetition*k.value for k in self.tiles.values])

    def len(self):
        return sum([k.repetition for k in self.tiles.values])

    def isAbleToForm(self, string):

class Alphabet(Word):
    def __init__(self, fichas):
        self.tiles = {k:Tile(k,r,v) for k, (r,v) in fichas.items()}
    def newWord(self, string):
        



class Scrabble():
    def __init__(self, language = 'es'):
        if language == 'es':
            fileName = 'palabras.words.gz'
            fichas = {'rr': (1, 8), 'll': (1, 8), 'u': (5, 1), 'o': (9, 1), 'v': (1, 4), 'ñ': (1, 8), 'q': (1, 5), 'g': (2, 2), 'e': (12, 1), 'd': (5, 2), 'y': (1, 4), 'b': (2, 3), 'h': (2, 4), 'p': (2, 3), 'c': (4, 3), 'n': (5, 1), 'x': (1, 8), 'a': (12, 1), 'r': (5, 1), 'blank': (2, 0), 's': (6, 1), 'l': (4, 1), 'ch': (1, 5), 'j': (1, 8), 'z': (1, 10), 'f': (1, 4), 't': (4, 1), 'i': (6, 1), 'm': (2, 3)}
        elif language == 'en':
            fileName = 'palabras_en.words.gz'
            fichas = {'u': (4, 1), 'o': (8, 1), 'k': (1, 5), 'v': (2, 4), 'q': (1, 10), 'l': (4, 1), 'g': (3, 2), 'e': (12, 1), 'd': (4, 2), 'y': (2, 4), 'b': (2, 3), 'h': (2, 4), 'p': (2, 3), 'c': (2, 3), 'n': (6, 1), 'x': (1, 8), 'a': (9, 1), 'r': (6, 1), 'blank': (2, 0), 's': (4, 1), 'w': (2, 4), 'j': (1, 8), 'z': (1, 10), 'f': (2, 4), 't': (6, 1), 'i': (9, 1), 'm': (2, 3)}
        else:
            raise NameError('Idioma no diponible')
        self.words = getWordsFromGZ(fileName)
        self.tiles = {k:Tile(k,r,v) for k, (r,v) in fichas.items()}
        self.language = language
        self.hand = {}
    
    def Solve(self, tiles, lenght=7):
        if len(tiles)<lenght:
            lenght = len(tiles) #maxima longitud de la palabra a formar
        
        for t in tiles:
            self.tiles[t].RemoveOne() #chequear que existan suficientes fichas
        
        
def getWordsFromGZ(fileName):
    with gzip.open(fileName,'rt',encoding='utf-8') as file:
        words = file.read().splitlines()
    words = [
        unicodedata.normalize('NFKD', w).encode('ASCII', 'ignore').decode('utf-8')
        for w in words 
        if w.islower()
        ] #remueve los nombres propios y reemplaza los caracteres con acento
    #TO DO: reemplazar RR LL CH?
    return words
def instring(a,b):

## TEST ##
scrabble = Scrabble()
print(scrabble.tiles['a'])
print(len(getWordsFromGZ('palabras.words.gz')))
# Idioma: es 
#fichas_es = {'rr': (1, 8), 'll': (1, 8), 'u': (5, 1), 'o': (9, 1), 'v': (1, 4), 'ñ': (1, 8), 'q': (1, 5), 'g': (2, 2), 'e': (12, 1), 'd': (5, 2), 'y': (1, 4), 'b': (2, 3), 'h': (2, 4), 'p': (2, 3), 'c': (4, 3), 'n': (5, 1), 'x': (1, 8), 'a': (12, 1), 'r': (5, 1), 'blank': (2, 0), 's': (6, 1), 'l': (4, 1), 'ch': (1, 5), 'j': (1, 8), 'z': (1, 10), 'f': (1, 4), 't': (4, 1), 'i': (6, 1), 'm': (2, 3)}

# Idioma: en 
#fichas_en = {'u': (4, 1), 'o': (8, 1), 'k': (1, 5), 'v': (2, 4), 'q': (1, 10), 'l': (4, 1), 'g': (3, 2), 'e': (12, 1), 'd': (4, 2), 'y': (2, 4), 'b': (2, 3), 'h': (2, 4), 'p': (2, 3), 'c': (2, 3), 'n': (6, 1), 'x': (1, 8), 'a': (9, 1), 'r': (6, 1), 'blank': (2, 0), 's': (4, 1), 'w': (2, 4), 'j': (1, 8), 'z': (1, 10), 'f': (2, 4), 't': (6, 1), 'i': (9, 1), 'm': (2, 3)}
