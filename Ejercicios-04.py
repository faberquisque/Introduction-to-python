'''1. Realice un programa para:'''
'''1.1. Leer los datos del archivo aluminio.dat y poner los datos del 
    elemento en un diccionario de la forma:
        d = {'S': 'Al', 'Z':13, 'A':27, 'M': '26.98153863(12)', 'P': 1.0000, 'MS':26.9815386(8)'}
'''
file=open('./data/aluminio.dat','r')
dataSTR=str.splitlines(file.read())
dictionary = dict(pair.split(' = ') for pair in dataSTR)
file.close()     
print(dictionary)
'''1.2. Modifique el programa anterior para que las masas sean números (float) 
    y descarte el valor de la incerteza (el número entre paréntesis)
'''
file=open('./data/aluminio.dat','r')
#dataSTR=str.splitlines(file.read())
dictionary = {}
for pair in str.splitlines(file.read()):
    key, value = pair.split(' = ')
    if value.find('(')>-1:
        dictionary[key]=value.split('(')[0]
    else:
        dictionary[key]=value
file.close()     
print(dictionary)

'''1.3. Agregue el código necesario para obtener una impresión de la forma:
    Elemento: S
    Número Atómico: 13
    Número de Masa: 27
    Masa: 26.98154
Note que la masa sólo debe contener 5 números decimales
'''
print('Elemento:', dictionary['Atomic Symbol'])
print('Número Atómico:', dictionary['Atomic Number'])
print('Número de Masa:', dictionary['Mass Number'])
print('Masa:', '{0:.8}'.format(dictionary['Standard Atomic Weight']))

'''2. Realice un programa para:'''
'''2.1. Leer el archivo elementos.dat y guardar los datos en un 
    diccionario, cuyas claves serán los símbolos del elemento:
        elementos.keys() = ['C', 'H', 'O', 'N', 'Na', 'Cl', 'Ca', 'Au']
    y los valores serán diccionarios tal como se definieron en el ejercicio 
    anterior. Por ejemplo:
        elementos['H'] = {'S': 'H', 'Z':1, 'A':1, 'M': 1.00782503207, 'P': 0.999885, 'MS':1.00794}
'''
file = open('./data/elementos.dat','r')
elementos = dict()
data = str.split(file.read(),sep='\n\n')
for elemento in data:
    caracteristicas = dict()
    for pair in elemento.splitlines():
        key, value = pair.split(' = ')
        if value.find('(')>-1:
            caracteristicas[key]=value.split('(')[0]
        else:
            caracteristicas[key]=value
    elementos[caracteristicas['Atomic Symbol']] = caracteristicas
file.close() 
for z in elementos: print(z)
'''2.2. Imprimir todos los elementos, en un formato legible (y si le sale: 
    agradable) para personas, ordenados en valores crecientes de masa.'''
lista1=sorted(elementos.values(), key=lambda a: int(a['Atomic Number']))
print('Elemento','N° Atomico','N° de Masa','Masa', sep='\t| ')
for z in lista1: print(z['Atomic Symbol'],z['Atomic Number'],z['Mass Number'],'{0: >#016.4f}'.format(float(z['Standard Atomic Weight'])),sep='\t\t| ')

'''3. PARA ENTREGAR: Adapte los programas realizados en el punto anterior 
    para trabajar con funciones. Se requiere que escriba:'''
'''3.1. Una función que lea un archivo (cuyo nombre es el argumento) y devuelva
    un diccionario donde cada clave es el símbolo del elemento.'''
def ReadElementsFile(fileName):
    '''lee el archivo #fileName y devuelve un diccionario donde cada clave es el simbolo del elemento'''        
    file = open('./data/elementos.dat','r')
    elementos = dict()
    data = str.split(file.read(),sep='\n\n')
    for elemento in data:
        caracteristicas = dict()
        for pair in elemento.splitlines():
            splittedPair = pair.split(' = ')
            if len(splittedPair) == 2:
                key, value = splittedPair 
                if value.find('(')>-1:
                    caracteristicas[key]=value.split('(')[0]
                #elif value.isnumeric:
                 #   caracteristicas[key] = int(value)
                else:
                    caracteristicas[key]=value
            else:
                print('Archivo mal escrito para carga de datos')
        elementos[caracteristicas['Atomic Symbol']] = caracteristicas
    file.close()
    return elementos
'''3.2. Una función que escriba en un string todos los elementos, ordenados 
    alfabéticamente por clave, en una forma similar a:
        s = 
        Elemento: C
        Z = 6
        A = 12
        Masa = 12.0000000
        Abundancia = 0.9893
        Masa Promedio = 12.0107

        Elemento: Ca
        Z = 20
        A = 40
        Masa = 39.96259098
        Abundancia = 0.96941
        Masa Promedio = 40.078

    Esta función tendrá un argumento requerido que es el diccionario con los 
    elementos y un argumento opcional reverse con valor por defecto False. Este 
    argumento indica si los elementos se ordenan alfabéticamente de la manera 
    natural (a,b,c...,y,z) o inversa (z,y,x, ... b,a).'''
def ElementsBySymbolToString(elementos,reverser=False):
    '''Escribe en un string todos los elementos ordenados alfabeticamente por clave a partir del diccionario. El parametro reverser invierte el orden'''
    listaOrdenada=sorted(elementos.values(),key=lambda a: a['Atomic Symbol'], reverse=reverser)
    s=list()
    for z in listaOrdenada:
        s.append('Elemento: '+z['Atomic Symbol']+'\n')
        s.append('Z = '+z['Atomic Number']+'\n')
        s.append('A = '+z['Mass Number']+'\n')
        s.append('Masa = '+'{0: >.4f}'.format(float(z['Relative Atomic Mass']))+'\n')
        s.append('Abundancia = '+'{0: >.3f}'.format(float(z['Isotopic Composition']))+'\n')
        s.append('Masa Promedio = '+'{0: >.4f}'.format(float(z['Standard Atomic Weight']))+'\n\n')
    return ''.join(s)
'''3.3. Una función que reciba un nombre de archivo y un string y escriba 
    el string en el archivo dado.'''
def WriteStringToFile(fileName, infoString):
    '''Escribe el string infoString en el archivo fileName'''
    import os
    os.makedirs(os.path.dirname(fileName), exist_ok=True)
    file = open(fileName,'w')    
    file.write(infoString)
    file.close()

'''3.4. Finalmente, escriba también el código llamando a las funciones 
    anteriores para realizar el trabajo de lectura y escritura de los elementos 
    en archivos.
'''
d=ReadElementsFile('elementos.dat')
s=ElementsBySymbolToString(d,False)
print(s)
WriteStringToFile('./output/elementos.dat',s)
'''4. Escriba funciones para analizar la divisibilidad de enteros:'''
'''4.1. La función es_divisible1(x) que retorna verdadero si x es divisible 
    por alguno de 2,3,5,7 o falso en caso contrario.'''
def es_divisible1(x):
    L=[2,3,5,7]
    flag=False
    for i in L:
        if x%i == 0:
            flag=True
    return flag

print(es_divisible1(13))
'''4.2. La función es_divisible_por_lista que cumple la misma función que 
    es_divisible1 pero recibe dos argumentos: el entero x y una variable del 
    tipo lista que contiene los valores para los cuáles debemos examinar la 
    divisibilidad. Las siguientes expresiones deben retornar el mismo valor:
        es_divisible1(x) 
        es_divisible_por_lista(x, [2,3,5,7])
        is_divisible_por_lista(x)
'''
def es_divisible_por_lista(x,lista):
    flag = False
    for i in lista:
        if x%i == 0:
            flag=True
    return flag
print(es_divisible_por_lista(13,[2,3,5,7]))
'''4.3. La función es_divisible_por cuyo primer argumento (mandatorio) es x, 
    y luego puede aceptar un número indeterminado de argumentos:
        es_divisible_por(x)  # retorna verdadero
        es_divisible_por(x, 2) # verdadero si x es par
        es_divisible_por(x, 2, 3, 5, 7) # igual resultado que es_divisible1(x)
        es_divisible_por(x, 2, 3, 5, 7, 9, 11, 13)  # o cualquier lista de argumentos debe funcionar
'''
def es_divisible_por(x, *lista):
    flag = False
    if len(lista)==0:
        flag=True
    else:
        for i in lista:
            if x%i == 0:
                flag=True
    return flag

print(es_divisible_por(13, 2, 3, 5, 7))
print(es_divisible_por(13))