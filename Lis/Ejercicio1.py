
# coding: utf-8

# In[40]:

'''1. Abra una terminal (consola) de Ipython y utilícela como una calculadora para:
*Suponiendo que, de las cuatro horas de clases, tomamos un descanso de 15 minutos y nos distraemos otros 13 minutos, 
calcular cuántos minutos efectivos de trabajo tendremos en las 16 clases.
*Para la cantidad de alumnos presentes en el aula: ¿cuántas horas-persona de trabajo hay involucradas?'''

minutos_clase=4*60
minutos_perdidos=(15+13)
clases=16
minutos_clase_efectivos=((minutos_clase-minutos_perdidos)*clases)
print(minutos_clase_efectivos)


# In[30]:

horas_de_clase=(minutos_clase_efectivos/60)
alumnos=80
horas_persona=(horas_de_clase*alumnos)
print(horas_persona)


# In[49]:

'''2. Muestre en la consola de Ipython:
*el nombre de su directorio actual
*los archivos en su directorio actual
*si está usando linux, la fecha y hora'''


# In[50]:

pwd


# In[51]:

ls


# In[52]:

cd prezi


# In[53]:

pwd


# In[54]:

'''3. Para cubos de lados de longitud L= 1, 3, 5 y 8,
calcule su superficie y su volumen.'''


# In[75]:

L=[1,3,5,8]
for i in L:
    Superficie=(i**2)*6
    print(Superficie, end=',')
print()
for i in L:
    Volumen=(i**3)
    print(Volumen, end=',')
    


# In[79]:

S=[]
for i in L:
    S.append(6*i**2)
print('Superficie=',S)


# In[81]:

V=[i**3 for i in L]
print('Volumen=', V)


# In[82]:

'''4. Para esferas de radios r= 1, 3, 5 y 8, calcule su superficie
y su volumen.'''


# In[98]:

from math import pi
r=[1,3,5,8]
s=[4*pi*j**2 for j in r]
print('superficie=',['{:.2f}'.format(i) for i in s])


# In[99]:

v=[4/3*pi*j**3 for j in r]
print('volumen=', ['{:.3f}'.format(i) for i in v])


# In[100]:

'''5. Abra un editor de textos y escriba las líneas necesarias para imprimir las siguientes frases (una por línea). Guarde y ejecute su programa.
Hola, por primera vez
Hola, hoy es mi día de escribir frases intrascendentes
Hola, nuevamente, y espero que por última vez
E = mc²
Adiós'''


# In[108]:

F=['Hola, por primera vez', 'Hola, hoy es mi día de escribir frases intrascendentes', 'Hola, nuevamente, y espero que por última vez', 'E = mc²', 'Adiós']
for i in F:
    print(i)
   


# In[ ]:



