import numpy as np
import matplotlib.pyplot as plt
print('Michel')
'''3. **PARA ENTREGAR:**Notando que la curva en color negro corresponde 
a la semisuma de las dos curvas en rojo, rehacer la siguiente figura:
(../figuras/ejercicio_08_3.png)'''

def pico(x,t=0, a=1, h=1):
  return h/2*picoAdimensional((x-t)/a)

def picoAdimensional(x):
    return np.piecewise(x, [-1>x, x>-1, x>0, x>1], [0,lambda x: 1+x,lambda x: 1-x,0])

a = 3
h = 4
x = np.linspace(-3*a,3*a,51,endpoint=True)
#vecPico = np.vectorize(pico)
T = [0, 0.3*a, 0.7*a, 1.2*a]
for i, t in enumerate(T):
    y1 = pico(x,t,a,h)
    plt.plot(x,y1,'r')
    y2 = pico(x,-t,a,h)
    plt.plot(x,y2,'r')
    y3 = y1+y2
    plt.plot(x,y3,'k--')
print(x)
print(y1)
plt.show()