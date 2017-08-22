'''3. PARA ENTREGAR: Adapte los programas realizados en el punto anterior 
    para trabajar con funciones. Se requiere que escriba:'''
'''3.1. Una función que lea un archivo (cuyo nombre es el argumento) y devuelva
    un diccionario donde cada clave es el símbolo del elemento.'''
def ReadElementsFile(fileName):
    '''lee el archivo #fileName y devuelve un diccionario donde cada clave es el simbolo del elemento'''        
    file = open(fileName,'r')
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