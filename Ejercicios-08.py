import numpy as np
import matplotlib.pyplot as plt
'''1. Para la función definida a trozos:
$$
f(x) =
\begin{cases}
  f_{1}(x) = x^{2}/8 & - \pi < x \le \pi/2  \\
  f_{2}(x) = -0.3 x  & \pi/2 < x < \pi \\
  f_{3}(x) = -(x - 2 \pi)^{2}/6 & \pi \le x \le 5 \pi/2 \\
  f_{4}(x) = (x - 2 \pi)/5 & 5 \pi/2 < x \le 3 \pi
  \end{cases}
$$
realizar la siguiente figura de la manera más fiel posible.
![](../figuras/ejercicio_08_1.png)
**Pistas:** Buscar información sobre `plt.fill_between()` y 
sobre `plt.xticks` y `plt.yticks`. 
'''
lim = [0,np.pi/2,np.pi,5/2*np.pi,3*np.pi]
def funcionPartida(x):
  lim = [-np.pi,np.pi/2,np.pi,5/2*np.pi,3*np.pi]
  if lim[0] < x and x <= lim[1]:
    return 1/8*x**2
  elif lim[1] < x and x < lim[2]:
    return -0.3*x
  elif lim[2] <= x and x <= lim[3]:
    return -1/6*(x-2*np.pi)**2
  elif lim[3] < x and x <= lim[4]:
    return (x-2*np.pi)/5
  else:
    return 0
vecFuncionPartida = np.vectorize(funcionPartida)
x = np.array([np.linspace(lim[i],lim[i+1],10) for i in range(len(lim)-1)])
print(x)
y = vecFuncionPartida(x)
print(y)
color = ['b','r','k','g']
for i in range(len(color)):
  plt.plot(x[i],y[i],color = color[i],ls = '-')
plt.show()
'''2. Rehacer la siguiente figura:
![](../figuras/ejercicio_08_2.png)
'''

'''3. **PARA ENTREGAR:**Notando que la curva en color negro corresponde 
a la semisuma de las dos curvas en rojo, rehacer la siguiente figura:
(../figuras/ejercicio_08_3.png)'''