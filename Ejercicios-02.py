# -*- coding: utf-8 -*-

'''5. Manejos de listas:'''
'''5.1. Cree la lista N de longitud 11, donde cada elemento es un número 
entero de 0 a 10 (Ayuda: vea la expresión range). '''
longitud=11
N=list(range(longitud))
print(N)
'''5.2. Invierta la lista.'''
N2=N[::-1]
print(N2)
'''5.3. Extraiga una lista N2 que contenga sólo los elementos pares de N.'''
print(N2[::2])
'''6. Cree una lista de la forma L = [1,3,5,...,19,19,17,...,3,1]'''
L1=list(range(1,20,2))
L2=L1[::-1]
print(L1+L2)
'''7. Operación "rara" sobre una lista:'''
'''7.1. Defina la lista L = [0,1]'''
L=[0,1]
'''7.2. Realice la operación L.append(L)'''
L.append(L)
'''7.3. Ahora imprima L, e imprima el último elemento de L.'''
print(L)
print(L[-1])
'''7.4. Haga que una nueva lista L1 que tenga el valor del último elemento de L y repita el inciso anterior.'''
L1=list(L[-1])
print(L1)
print(L1[-1])
'''8. Utilizando el string: '''
s1='En un lugar de la Mancha de cuyo nombre no quiero acordarme' 
'''y utilizando los métodos de strings:'''
'''8.1. Obtenga la cantidad de caracteres.'''
S=list(s1)
print(len(S))
'''8.2. Imprima la frase anterior pero con cada palabra empezando en mayúsculas.'''
S_mayus=S.copy()
for j in range(len(S_mayus)):
    if S_mayus[j]==' ':
        S_mayus[j+1]=S_mayus[j+1].upper()
print(''.join(S_mayus))
'''8.3. Cuente cuantas letras 'a' tiene la frase, ¿cuántas vocales tiene?'''
print(S.count('a'))
vocales=['a','e','i','o','u']
cantidad=0
for v in vocales:
    cantidad=cantidad+s1.lower().count(v)
print(cantidad)
'''8.4. Imprima el string s1 centrado en una línea de 80 caracteres, rodeado de guiones en la forma:
   ----------En un lugar de la Mancha de cuyo nombre no quiero acordarme-----------
'''
'''8.5. Obtenga una lista L1 donde cada elemento sea una palabra.'''
'''8.6. Cuente la cantidad de palabras en s1 (utilizando python).'''
'''8.6. Ordene la lista L1 en orden alfabético.'''
'''8.6. Ordene la lista L1 tal que las palabras más cortas estén primero.'''
'''8.6. Ordene la lista L1 tal que las palabras más largas estén primero.'''
'''8.6. Construya un string s2 con la lista del resultado del punto anterior.'''
'''8.6. Encuentre la palabra más larga y la más corta de la frase.'''
'''9. Escriba un script (llamado distancia1.py) que defina las variables velocidad y posición inicial,
   la aceleración g, y la masa kg a tiempo t_0, y calcule e imprima la posición y velocidad a un tiempo posterior t.
   Ejecute el programa para varios valores de posición y velocidad inicial para segundos. 
   Recuerde que las ecuaciones de movimiento con aceleración constante son:'''

'''10. Calcular la suma:
   Ayuda: busque información sobre la función sum()'''