import numpy as np
import math
import matplotlib.pyplot as plt
''' 1. Crear una función para calcular el valor de $\pi$ usando el "método de cociente de áreas". Para ello:

      * Generar puntos en el plano dentro del cuadrado de lado unidad cuyo lado inferior va de $x=0$ a $x=1$
      * Contar cuantos puntos caen dentro del (cuarto de) círculo unidad. Este número tiende a ser proporcional al área del círculo
      * La estimación de $\pi$ será igual a cuatro veces el cociente de números dentro del círculo dividido por el número total de puntos.
'''
def metodoCocienteAreas(n=1000):
    L=np.random.random((2,n))
    Z=L[0]**2+L[1]**2
    return 4*len(Z[np.where(Z < 1)])/n
'''2. Crear una función para calcular el valor de $\pi$ usando el "método del valor medio":
       Este método se basa en la idea de que el valor medio de una función se puede calcular de la siguiente manera:

$$ \langle f \rangle = \frac{1}{b-a} \int_{a}^{b} f(x)\, dx $$

Tomando la función particular $f(x)= \sqrt{1- x^{2}}$ entre $x=0$ y $x=1$, obtenemos:

$$ \langle f \rangle = \int_{0}^{1} \sqrt{1- x^{2}}\, dx = \frac{\pi}{4} $$

Entonces, tenemos que estimar el valor medio de la función $f$ y, mediante la relación anterior obtener $\pi = 4 \langle f(x) \rangle$. Para 
obtener el valor medio de la función notamos que si tomamos $X$ es una variable aleatoria entre 0 y 1, entonces el valor medio de $f(X)$ es 
justamente $\langle f \rangle$. Su función debe entonces

    * Generar puntos aleatoriamente en el intervalo $[0,1]$
    * Calcular el valor medio de $f(x)$ para los puntos aleatorios $x$.
'''
def funcion(x):
    return math.sqrt(1-x**2)
def metodoValorMedio(n=1000):
    x=np.random.random(n)
    y=np.array([funcion(k) for k in x])
    return np.mean(y)*4
'''3. Utilizar las funciones anteriores con diferentes valores para el número total de puntos $N$. En particular, hacerlo para 20 valores de $N$ 
equiespaciados logarítmicamente entre 100 y 10000. Para cada valor de $N$ calcular la estimación de $\pi$. Realizar un gráfico con el valor 
estimado como función del número $N$ con los dos métodos (dos curvas en un solo gráfico)
'''
def comparacionMetodos(start=2,stop=4,num=20):
    N=np.logspace(start,stop,num)
    pi1=np.array([metodoCocienteAreas(int(n)) for n in N])
    pi2=np.array([metodoValorMedio(int(n)) for n in N])
    plt.semilogx(N,pi1)
    plt.semilogx(N,pi2)
    plt.grid(True)
    plt.show()

'''4. Para $N=15000$ repetir el "experimento" muchas veces (al menos 1000) y realizar un histograma de los valores obtenidos para $\pi$ con cada 
método. Graficar el histograma y calcular la desviación standard. Superponer una función Gaussiana con el mismo ancho. El gráfico debe ser 
similar al siguiente (*el estilo de graficación no tiene que ser el mismo*)

![](../figuras/ejercicio_09_1.png)
'''
def normal(x,mean,sigma):
    return math.exp(-((x-mean)**2)/2/sigma**2)/math.sqrt(2*math.pi*sigma**2)
def comparacionPorHistograma():
    N=15000
    repetir=1000
    pi1=np.array([metodoCocienteAreas(N) for i in range(repetir)])
    pi2=np.array([metodoValorMedio(N) for i in range(repetir)])
    mean1=np.mean(pi1)
    mean2=np.mean(pi2)
    desv1=np.std(pi1)
    desv2=np.std(pi2)
    x=np.linspace(3.05,3.25,100)
    normal1=np.array([normal(k,mean1,desv1) for k in x])
    normal2=np.array([normal(k,mean2,desv2) for k in x])
    plt.plot(x,normal1)
    plt.plot(x,normal2)
    plt.show()
    

'''5. El método de la aguja del bufón se puede utilizar para estimar el valor de $\pi$, y consiste en tirar agujas (o palitos, fósforos, etc) 
al azar sobre una superficie rayada

![](../figuras/Streicholz-Pi-wiki.jpg)

Por simplicidad vamos a considerar que la distancia entre rayas $t$ es mayor que la longitud de las agujas $\ell$

![](../figuras/Buffon_needle_wiki.png)

La probabilidad de que una aguja cruce una línea será:

$$ P = \frac{2 \ell}{t\, \pi} $$

por lo que podemos calcular el valor de $\pi$ si estimamos la probabilidad $P$. Realizar una función que estime $\pi$ utilizando este método y 
repetir las comparaciones de los dos puntos anteriores pero ahora utilizando este método y el de las áreas.
'''

print(metodoCocienteAreas())
print(metodoValorMedio())
#comparacionMetodos()
comparacionPorHistograma()
print('finished!')