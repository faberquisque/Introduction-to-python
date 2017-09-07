import numpy as np
'''Escriba una función suma_potencias(p, n) (utilizando Numpy) que calcule la operación
s_2=sum_0^n k^p
'''
def suma_potencias(p, n):
    ''' Devuelve la sumatoria de k^p para k entre 0 y n'''
    a = np.array(range(n+1))
    return sum(a**p)
'''Modifique la función `caida_libre` de una práctica anterior para que acepte
un array de tiempos y devuelva un array con las velocidades $v(t)$ y otro con
las posiciones $h(t)$ en lugar de un único valor.
'''
def caida_libre(t=1, z_0=0, v_0=0, g=9.81, m=1):
    '''devuelve un tuple con la posicion y la velocidad'''
    v=v_0-g*t#m/s
    z=z_0+v_0*t-g/2*t**2#m
    return z, v 
'''3. **Integration por trapecios:**  Queremos realizar numéricamente la integral
  $$
  \int_{a}^{b}f(x)dx
  $$

  utilizando el método de los trapecios. Para eso partimos el intervalo $[a,b]$ en N 
  subintervalos y aproximamos la curva en cada subintervalo por una recta

![](../figuras/trapez_rule_wiki.png)

  La línea azul representa la función $f(x)$ y la línea roja la interpolación por una 
  recta (figura de https://en.wikipedia.org/wiki/Trapezoidal_rule)

  Si llamamos $x_{i}$ ($i=0,\ldots,n,$ con $x_{0}=a$ y $x_{n}=b$) los puntos 
  equiespaciados, entonces queda
  $$
     \int_{a}^{b}f(x)dx\approx\frac{h}{2}\sum_{i=1}^{n}\left(f(x_{i})+f(x_{i-1})\right).
  $$
'''

'''3.1. Escriba una función  `trapz(x, y)` que reciba dos array unidimensionales `x` e `y` 
y aplique la fórmula de los trapecios'''

def trapz(x,y):
    h=x[1::]-x[:-1:]
    f=y[1::]+y[:-1:]
    return sum(h*f/2)

'''3.2. Escriba una función `trapzf(f, a, b, npts=100)` que recibe una función `f`, los 
límites `a`, `b` y el número de puntos a utilizar `npts`, y devuelve el valor de la 
integral por trapecios.'''

def trapzf(f, a, b, npts = 100):
    x = np.linspace(a, b, npts, endpoint=True)
    y = f(x)
    return trapz(x,y)
'''------TEST------'''
print(suma_potencias(1,6))

print(caida_libre(1.2))

a = np.arange(0,10.5,0.5)
z,v = caida_libre(a)
print(z)
print(v)

y = a**2

print(trapz(a,y))

def testFun(x):
    return x**2

print(trapzf(testFun, 0, 10, 21))