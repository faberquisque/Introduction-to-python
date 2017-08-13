# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
"""
Ejercicio 1:
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
print("cantidad de palabras:",s.count(" ")+1)

"""
Forme un nuevo string de 10 caracteres que contenga los 5 primeros y los 5 
últimos del string anterior s.
"""
print("Solucion:",s[:5]+s[-5:])

"""
Forme un nuevo string que contenga los 10 caracteres centrales de s 
(utilizando un método que pueda aplicarse a otros strings también).
"""
n=10
z=(len(s)-n)/2
extracto=s[math.floor(z):-math.ceil(z)]
print(extracto)
print(len(extracto))

"""
Cambie todas las letras "a" por "e" y todas las letras "e" por "a" 
en el string s
"""
