'''1. Abra una terminal (consola) de Ipython y utilícela como una calculadora para:'''
'''1.1. Suponiendo que, de las cuatro horas de clases, 
tomamos un descanso de 15 minutos y nos distraemos otros 13 minutos, 
calcular cuántos minutos efectivos de trabajo tendremos en las 16 clases.'''
horas_clase=4 #horas de clase
minutos_hora=60 #minutos en una hora
descanso=15 #minutos por descanso
distraccion=13 #minutos desperdiciados
clases=16 #clases en el curso
minutos_efectivos=(horas_clase*minutos_hora-descanso-distraccion)*clases
print(minutos_efectivos)
'''1.2. Para la cantidad de alumnos presentes en el aula: ¿cuántas horas-persona de trabajo hay involucradas?'''
alumnos= 80 #numero de alumnos
horas_persona=alumnos*minutos_efectivos/minutos_hora
print(horas_persona)
'''2. Muestre en la consola de Ipython:'''
'''2.1. el nombre de su directorio actual'''
import os
print(os.getcwd())
'''2.2. los archivos en su directorio actual'''
print(os.listdir())
'''2.3. si está usando linux, la fecha y hora'''
import datetime
print(datetime.datetime.now().date())
print(datetime.datetime.now().time())
'''3. Para cubos de lados de longitud L= 1, 3, 5 y 8, calcule su superficie y su volumen.'''
L=[1,3,5,8]
for i in L:
    print('cubo de lado:',i)
    print('  superficie:',6*i**2)
    print('     volumen:',i**3)
'''4. Para esferas de radios r= 1, 3, 5 y 8, calcule su superficie y su volumen.'''
r= [1, 3, 5, 8]
for j in r:
    print('esfera de radio:',j)
    print('     superficie:',4*3.1415*j**2)
    print('        volumen:',4/3*3.1415*j**3)
'''5. Abra un editor de textos y escriba las líneas necesarias para imprimir las 
siguientes frases (una por línea). Guarde y ejecute su programa.'''
'''5.1. Hola, por primera vez'''
print('Hola, por primera vez')
'''5.2. Hola, hoy es mi día de escribir frases intrascendentes'''
print('Hola, hoy es mi día de escribir frases intrascendentes')
'''5.3. Hola, nuevamente, y espero que por última vez'''
print('Hola, nuevamente, y espero que por última vez')
'''5.4. E = mc²'''
print('E = mc²')
'''5.5. Adiós'''
print('Adiós')