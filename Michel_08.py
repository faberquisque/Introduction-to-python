import numpy as np
import matplotlib.pyplot as plt
print('Michel')
'''3. **PARA ENTREGAR:**Notando que la curva en color negro corresponde 
a la semisuma de las dos curvas en rojo, rehacer la siguiente figura:
(../figuras/ejercicio_08_3.png)'''

def pico(x,t,a,h):
  return h/2*picoAdimensional((x-t)/a)

def picoAdimensional(x):
  if x < -1:
    return 0
  elif -1 <= x and x < 0:
    return 1+x
  elif 0 <= x and x < 1:
    return 1-x
  elif x > 1:
    return 0
  else:
    return 0

a = 3
h = 4
x = np.linspace(-3*a,3*a,51,endpoint=True)
vecPico = np.vectorize(pico)
T = [0, 0.3*a, 0.7*a, 1.2*a]
for i, t in enumerate(T):
    y1 = np.array([pico(k,t,a,h) for k in np.nditer(x)])
    plt.plot(x,y1,'r')
    y2 = np.array([pico(k,-t,a,h) for k in np.nditer(x)])
    plt.plot(x,y2,'r')
    y3 = y1+y2
    plt.plot(x,y3,'k--')
print(x)
print(y1)
plt.show()