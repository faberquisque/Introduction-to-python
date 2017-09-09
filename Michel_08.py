import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', family='serif', size=14)
rc('text', usetex=True)
'''3. **PARA ENTREGAR:**Notando que la curva en color negro corresponde 
a la semisuma de las dos curvas en rojo, rehacer la siguiente figura:
(../figuras/ejercicio_08_3.png)'''

def pico(x,t=0, a=1, h=1):
  return h/2*picoAdimensional((x-t)/a)

def picoAdimensional(x):
    return np.piecewise(x, [-1>x, x>-1, x>0, x>1], [0,lambda x: 1+x,lambda x: 1-x,0])

a = 3
h = 4
x = np.linspace(-3*a,3*a,501,endpoint=True)
#vecPico = np.vectorize(pico)
T = [0, 0.3*a, 0.7*a, 1.2*a]
annotations = [r'$t=0$',r'$t<a/2$',r'$t>a/2$',r'$t>a$']
fig, axes = plt.subplots(2, 2, sharex='col', sharey='row')

fig.subplots_adjust(hspace=0, wspace=0)
plt.setp(axes, xticks=[-2*a,-a, 0., a,2*a], xticklabels=[r'-$2a$', r'$-a$', r'$0$',r'$a$',r'$2a$'])
plt.setp(axes, yticks=[0,h/2,h], yticklabels=[r'$0$',r'$h/2$',r'$h$'])
#plt.setp(axes, xlabel=r'$x$', ylabel=r'$u(x,t)$')
for i, t in enumerate(T):
    c = i%2         #numero de columna
    f = int(i/2)%2  #numero de fila
    ax =  axes[f][c]
    ax.tick_params(direction='in')
    y1 = pico(x,t,a,h)
    y2 = pico(x,-t,a,h)
    if i != 0:
        ax.plot(x,y1,'r')
        ax.plot(x,y2,'r')
    if c == 0:
        ax.set_ylabel(r'$u(x,t)$', fontsize=20)
    else:
        ax.tick_params('y',direction='out')
    if f == 0:
        ax.get_yticklabels()[0].set_visible(False)
        ax.tick_params('x', direction='out')
        #ax.tick_params('x',direction='out')
    else:
        ax.tick_params('x',top='on')
        ax.set_xlabel(r'$x$', fontsize=20)
    y3 = y1+y2
    ax.plot(x,y3,'k--')
    ax.annotate(annotations[i], xy=(a, 2/3*h))
    ax.set_xlim([-3*a,3*a])
    ax.set_ylim([0,h])
#fig.tight_layout()
plt.show()