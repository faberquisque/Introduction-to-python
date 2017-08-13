# -*- coding: utf-8 -*-
"""
entrega-clase-2-GM.py
"""
import math
"""
Cuente la cantidad de veces que aparece un substring en un dado string. 
Hágalo en los dos casos: distinguiendo entre mayúsculas y minúsculas, y 
no distinguiendo. Realícelo, buscando los substrings es, la, que, co, en 
el string. Cuente cuántas palabras tiene el string.
"""
s = "Aquí me pongo a cantar Al compás de la vigüela, Que el hombre que lo desvela Una pena estraordinaria Como la ave solitaria Con el cantar se consuela."

#print(s)
m=["es","la","que","co"]

# se cuentan las apariciones de los substrings en el string s, case-sensitive y case-insensitive
for j in m:
    print(j,'->',"sensitive",s.count(j),"insensitive",s.lower().count(j))
    
# se cuentan las palabras contando los espacios + 1 
print("Cantidad de palabras en s:",s.count(" ")+1)

"""
Forme un nuevo string de 10 caracteres que contenga los 5 primeros y los 5 
últimos del string anterior s.
"""
print("Los 5 primero y los 5 ultimos caracteres:",s[:5]+s[-5:])

"""
Forme un nuevo string que contenga los 10 caracteres centrales de s 
(utilizando un método que pueda aplicarse a otros strings también).
"""
n=10
z=(len(s)-n)/2
extracto=s[math.floor(z):-math.ceil(z)]
print('Los',len(extracto),'caracteres centrales:',extracto)

"""
Cambie todas las letras "a" por "e" y todas las letras "e" por "a" 
en el string s
"""
S=list(s)
for i in range(len(S)):
    if S[i]=='a':
        S[i]='e'
    elif S[i]=='e':
        S[i]='a'
print('Nuevo string con los caracteres a y e intercambiados')
print(''.join(S))