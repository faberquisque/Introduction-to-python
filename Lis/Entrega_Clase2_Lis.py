# -*- coding: utf-8 -*-
"""
Archivo de clase 2: 
"""

"""
Calcule el ángulo interior del polígono regular de 
<math>N</math> lados (por ejemplo el de un triángulo 
es 60 grados, de un cuadrado es 90 grados, y de un pentágono
es 108 grados). Exprese el resultado en grados y en radianes
para valores de <math>N= 3, 5, 6, 8, 9, 10, 12</math>
"""

#Primera aproximación para el triángulo

n=3
alfa=360/n
beta=180-alfa
print(beta)


#Para todos en grados

n=[3, 5, 6, 8, 9, 10, 12]#n es un vector
for j in n:# para cada elemento en el vector j ejecutar los siguientes comandos
    alfa=360/j
    beta=180-alfa
    print(beta)#si no le pongo "deg" no aparecen las unidades

#Para todos en grados y radianes

import math #para poder dar los valores en radianes
n=list([3, 5, 6, 8, 9, 10, 12])#no es necesario el comando list como se hizo arriba
for j in n:
    alfa=360/j
    beta=180-alfa
    print(beta,"deg",math.radians(beta),"rad")
    
"""
¿Puede calcular la longitud del lado de los polígonos 
regulares si se encuentran inscriptos en un círculo de 
radio unidad?
"""
n=[3, 5, 6, 8, 9, 10, 12]
for j in n:
    alfa=360/j
    c=math.sqrt(2*(1-math.cos(math.radians(alfa))))
    print(c)
    
"""
Cuente la cantidad de veces que aparece un substring en un dado
string. Hágalo en los dos casos: distinguiendo entre mayúsculas
y minúsculas, y no distinguiendo. Realícelo, buscando los 
substrings es, la, que, co, en el string. Cuente cuántas 
palabras tiene el string.
"""
s = "Aquí me pongo a cantar Al compás de la vigüela, Que el hombre que lo desvela Una pena estraordinaria Como la ave solitaria Con el cantar se consuela."#este es el string
print(s)
#Aca solo cuenta las minusculas
print(s.count("es"))#lo que busca es las letras consecutivas es, no la palabra es, si querés esto tenés que poner " es "
print(s.count("la"))
print(s.count("que"))#solo lo lee en minusculas, no cuenta la vez que aparece en mayuscula
print(s.count("co"))

m=["es","la","que","co"]
for j in m:
    print(j)
for j in m:
    print(s.count(j))
for j in m:
    print(j,"->",s.count(j))
    
#Ahora contando minúsculas y mayúsculas: tenemos que encontrar una función que convierta todo a minúsculas
for j in m:
    print(j,"->","sensitive:",s.count(j),"insensitive:",s.lower().count(j)) #control+i para ver la ayuda de que es la función .lower

#Cuento cuantas paralbras hay: es más fácil contar los espacios, hay n+1 palabras si n=espacios
print(s.count(" ")+1)

"""Forme un nuevo string de 10 caracteres que contenga los 5 primeros y los 5 últimos del string anterior s.
"""

print(s[0:5]+s[-5:])#s[i:j], i es el inicio y j es el final(no incluido)

"""Forme un nuevo string que contenga los 10 caracteres centrales de s (utilizando un método que pueda aplicarse a otros strings también)
"""
n=10
z=((len(s)-n)/2)#el int es para convertir el número a un entero
extracto=s[math.ceil(z):-math.floor(z)]
print(extracto)
print(len(extracto))

""" 
Cambie todas las 
letras "a" por "e" y todas las letras "e" por "a" en el string s
"""
#hola nadia