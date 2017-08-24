'''1. Calcule la suma
s2=∑_{k=1}^∞ (−1)^k(k+1)/(2k^3+k^2)
 
con un error relativo estimado menor a  ϵ=10−5 . 
Imprima por pantalla el resultado, el valor máximo de  k  
computado y el error relativo estimado.'''
TOL=1.0e-5
s=0
k=1
e=1
while e>TOL:
    s_k = (-1)**k * (k+1) / (2*k**3+k**2)
    s+=s_k
    e=abs(s_k)
    k+=1
print(s,k)
'''2. Realice un programa que:
    Lea el archivo names.txt
    Guarde en un nuevo archivo (llamado pares.txt) palabra por medio del archivo original (la primera, tercera, ...) una por línea, pero en el orden inverso al leído
    Agregue al final de dicho archivo, las palabras pares pero separadas por un punto y coma (;)
    En un archivo llamado longitudes.txt guarde las palabras ordenadas por su longitud, y para cada longitud ordenadas alfabéticamente.
    En un archivo llamado letras.txt guarde sólo aquellas palabras que contienen las letras w,x,y,z, con el formato:
    w: Walter, ....
    x: Xilofón, ...
    y: ....
    z: ....
'''
fileToRead = open('.\\data\\names.txt','r')
nombres = (fileToRead.read()).splitlines()
fileToRead.close()

import os
os.makedirs(os.path.dirname('.\output\pares.txt'), exist_ok=True) # crea el directorio si no existe
fileParesToWrite = open('.\output\pares.txt','w')    
fileParesToWrite.write('\n'.join(nombres[-1::-2]))
fileParesToWrite.write('\n')
fileParesToWrite.write('; '.join(nombres[1::2]))
fileParesToWrite.close()

nombres_alfa = sorted(nombres)
nombres_len = sorted(nombres_alfa, key=len)
fileLongitudesToWrite = open('.\\output\\longitudes.txt','w')
fileLongitudesToWrite.write('\n'.join(nombres_len))
fileLongitudesToWrite.close()

nombres_wxyz = dict()
listLetras = list(['w', 'x', 'y', 'z'])
for letra in listLetras:
        nombres_wxyz[letra]=list()
for name in nombres:
    for letra in listLetras:
        if letra in name.lower():
            (nombres_wxyz[letra]).append(name)
fileLetrasToWrite = open('.\\output\\letras.txt','w')
for key in nombres_wxyz.keys():
    fileLetrasToWrite.write(key+': ')
    fileLetrasToWrite.write(', '.join(nombres_wxyz[key]))
    fileLetrasToWrite.write('\n')
fileLetrasToWrite.close()
'''3. Cree dos listas: una con los números que no son múltiplos 
de ninguno de 2,7,11,13 y otra con los que no son múltiplos 
de 3,5,17. Considere los primeros 5000 números naturales. Cree 
una nueva lista donde combine las dos listas anteriores ordenada 
en forma creciente.
'''
TOP=5000
lista1 = [2,7,11,13]
lista2 = [3,5,17]
multiplos1 = list()
multiplos2 = list()
for i in range(2,TOP):
    for j in lista1:
        if i%j == 0:
            multiplos1.append(i)
    for j in lista2:
        if i%j ==0:
            multiplos2.append(i)
multiplos=multiplos1+multiplos2
multiplos.sort()
print(set(multiplos))
'''4. Las funciones de Bessel de orden  nn  cumplen las 
relaciones de recurrencia
J_{n−1}(x)−2*n/x*J_n(x)+J_{n+1}(x)=0
J_0^2(x)+∑_{n=1}^∞ 2*J_{2n}^2(x)=1
 
Para calcular la función de Bessel de orden  N , se empieza con un 
valor de  M≫N , y utilizando los valores iniciales  J_M=1, J_{M+1}=0
se utiliza la primera relación para calcular todos los valores 
de  n<M . Luego, utilizando la segunda relación se normalizan 
todos los valores. Nota: Estas relaciones son válidas si  M≫x
(use algún valor estimado, como por ejemplo  M=N+20 ).
Utilice estas relaciones para calcular  J_N(x)  para  
N=3,4,7 y  x=2.5,5.7,10. Para referencia se dan los valores esperados
J_3(2.5)=0.21660
J_4(2.5)=0.07378
J_7(2.5)=0.00078
J_3(5.7)=0.20228
J_4(5.7)=0.38659
J_7(5.7)=0.10270
J_3(10.0)=0.05838
J_4(10.0)=−0.21960
J_7(10.0)=0.21671
'''

'''5. Escriba un script distancia2.py que guarde en dos vectores 
(listas) v y z, 100 velocidades y posiciones de una pelota de 
masa m=1 con condiciones iniciales  z0=500  m y  v0=0  m/s, como 
función del tiempo, para tiempos t entre 0 y 10 segundos. El script p
uede ser ejecutado desde IPython con el comando mágico 
%run nombre_del_script. Luego los vectores v y z estarán disponibles 
durante la sesión.
'''

'''6. Imprima por pantalla una tabla con valores equiespaciados de 
x entre 0 y 180, con valores de las funciones trigonométricas de 
la forma:

|=================================|
| x  | sen(x) | cos(x) | tan(-x/4)|
|=================================|
|  0 |  0.000 |  1.000 |  -0.000  |
| 10 |  0.174 |  0.985 |  -0.044  |
| 20 |  0.342 |  0.940 |  -0.087  |
| 30 |  0.500 |  0.866 |  -0.132  |
| 40 |  0.643 |  0.766 |  -0.176  |
| 50 |  0.766 |  0.643 |  -0.222  |
| 60 |  0.866 |  0.500 |  -0.268  |
| 70 |  0.940 |  0.342 |  -0.315  |
| 80 |  0.985 |  0.174 |  -0.364  |
| 90 |  1.000 |  0.000 |  -0.414  |
|100 |  0.985 | -0.174 |  -0.466  |
|110 |  0.940 | -0.342 |  -0.521  |
|120 |  0.866 | -0.500 |  -0.577  |
|130 |  0.766 | -0.643 |  -0.637  |
|140 |  0.643 | -0.766 |  -0.700  |
|150 |  0.500 | -0.866 |  -0.767  |
|160 |  0.342 | -0.940 |  -0.839  |
|170 |  0.174 | -0.985 |  -0.916  |
|=================================|
'''

'''7. Dada una lista de números, vamos a calcular valores relacionados 
a su estadística.'''
'''Calcular los valores de la media aritmética, la media geométrica y la media armónica, dados por:
A(x1,…,xn)=x_med=(x_1+⋯+x_n)/n
G(x1,…,xn)=power(prod(x_1⋯x_n),1/n)
H(x1,…,xn)=n/(x1^{-1}+⋯+x_n^{n})
'''
def media(lista):
    return sum(lista)/len(lista)
def geometrica(lista):
    prod=1
    for i in lista:
        prod *=i
    return prod**(1/len(lista))
def armonica(lista):
    arm=0
    for i in lista:
        arm += 1/i
    return len(lista)/arm
'''Calcular la desviación estándard:
σ≡^sqrt(1/n*∑_i (xi−x_med)^2)
'''
 def desviacion(lista)
    desv=0
    prom=media(lista)
    for i in lista
        desv += (i-prom)**2
    return (desv/len(lista))**0.5
'''Calcular la mediana, que se define como el valor para el 
cual la mitad de los valores de la lista es menor que ella. Si el 
número de elementos es par, se toma el promedio entre los dos 
adyacentes.'''
'''7.1. Realizar los cálculos para las listas de números:
L1 = [6.41, 1.28, 11.54, 5.13, 8.97, 3.84, 10.26, 14.1, 12.82, 16.67, 2.56, 17.95, 7.69, 15.39]
L2 = [4.79, 1.59, 2.13, 4.26, 3.72, 1.06, 6.92, 3.19, 5.32, 2.66, 5.85, 6.39, 0.53]
'''
'''7.2. La moda se define como el valor que ocurre más frecuentemente en 
una colección. Note que la moda puede no ser única. En ese caso debe 
obtener todos los valores. Calcule la moda de las siguientes listas de 
números enteros:
L = [8, 9, 10, 11, 10, 6, 10, 17, 8, 8, 5, 10, 14, 7, 9, 12, 8, 17, 10, 12, 9, 11, 9, 12, 11, 11, 6, 9, 12, 5, 12, 9, 10, 16, 8, 4, 5, 8, 11, 12]
'''

'''8. Dada una lista de direcciones en el plano, expresadas por los 
ángulos en grados a partir de un cierto eje, calcular la dirección 
promedio, expresada en ángulos. Pruebe su algoritmo con las listas:
t1 = [0, 180, 370, 10]
t2 = [30, 0, 80, 180]
t3 = [80, 180, 540, 280]
'''