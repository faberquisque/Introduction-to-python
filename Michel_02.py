# -*- coding: utf-8 -*-
"""
entrega-clase-2-GM.py
"""
import math

#imprimir nombre y apellido:
print("Gaston Michel")
print("Ejercicio 4")

"""
Cuente la cantidad de veces que aparece un substring en un dado string. 
Hágalo en los dos casos: distinguiendo entre mayúsculas y minúsculas, y 
no distinguiendo. Realícelo, buscando los substrings es, la, que, co, en 
el string. Cuente cuántas palabras tiene el string.
"""
s = "Aquí me pongo a cantar\nAl compás de la vigüela,\nQue el hombre que lo desvela\nUna pena estraordinaria\nComo la ave solitaria\nCon el cantar se consuela."

#print(s)
m=["es","la","que","co"]

# se cuentan las apariciones de los substrings en el string s, case-sensitive y case-insensitive
print("Distinguiendo:",end=' ')
for j in m:
    print(s.count(j),end=' ')

print()
print("Sin distinguir:",end=' ') 
for j in m:
    print(s.lower().count(j),end=' ')

print()
# se cuentan las palabras contando los espacios + 1 
#print("Cantidad de palabras en s:",s.count(" ")+1)

"""
Forme un nuevo string de 10 caracteres que contenga los 5 primeros y los 5 
últimos del string anterior s.
"""
print(s[:5]+s[-5:])

"""
Forme un nuevo string que contenga los 10 caracteres centrales de s 
(utilizando un método que pueda aplicarse a otros strings también).
"""
n=10
z=(len(s)-n)/2
extracto=s[math.floor(z):-math.floor(z)]
print(extracto)

"""
Cambie todas las letras "m" por "n" y todas las letras "n" por "n" 
en el string s
"""
S=list(s)
for i in range(len(S)):
    if S[i]=='n':
        S[i]='m'
    elif S[i]=='m':
        S[i]='n'

print(''.join(S))