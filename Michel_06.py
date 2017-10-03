class Polinomio:

  def __init__(self, coefs=[]):
    """Crea el objeto. Si los coeficientes son proporcionados lo inicializa
    Keyword Arguments:
    coefs -- (default [])
    """
    if len(coefs)<10:
      self.coeficientes=coefs
    else:
      print('ERROR: polinomio de grado mayor que 9')
    return None
  

  def set_coeficientes(self, coefs=[]):
    """Si los coeficientes son proporcionados lo inicializa
    Keyword Arguments:
    coefs -- Una lista de coeficientes
    """
    if len(coefs)<10:
      self.coeficientes=coefs
    else:
      print('ERROR: polinomio de grado mayor que 9')

  def grado(self):
    "Devuelve el grado del polinomio (un entero)"
    return len(self.coeficientes)-1

  def get_coeficientes(self):
    """Devuelve los coeficientes del polinomio """
    return self.coeficientes

  def suma_pol(self, p1):
    """Al polinomio le suma el polinomio `p1` y devuelve un nuevo polinomio
    Keyword Arguments:
    p1 -- Polinomio a sumar
    """
    from itertools import zip_longest
    return Polinomio([x+y for x,y in zip_longest(self.coeficientes, p1.coeficientes, fillvalue=0)])

  def derivada(self, n=1):
    """Devuelve la derivada (n-ésima) del polinomio (un nuevo polinomio)
    Keyword Arguments:
    n -- (default 1) Orden de derivación

    Modo de uso:
    >>> P = Polinomio([0.1,2,3,0,1])
    >>> P1 = P.derivada()
    >>> P2 = P.derivada(n=2)
    """
    if n > self.grado():
      return Polinomio([0])   #solucion trivial
    result = Polinomio([x*y for x,y in enumerate(self.coeficientes)][1::])
    if n==1:
      return result
    else:
      return result.derivada(n-1)
    

  def integrada(self, n=1,cte=(0,)):
    """Devuelve la antiderivada (n-ésima) del polinomio (un nuevo polinomio)

    Keyword Arguments:
    n -- (default 1) Orden de integración
    cte -- (default 0) Constante de integración (tuple)

    Modo de uso:
    >>> P = Polinomio([0.1,2,3,0,1)
    >>> P1 = P.integrada()
    >>> P2 = P.integrada(cte=1.2, n=2)
    """
    if n > len(cte):
      cte=cte+(0,)
    result = Polinomio([cte[0], self.coeficientes[0]]+[a/(i+1) for i,a in list(enumerate(self.coeficientes))[1::]])
    if n==1:
      return result
    else:
      return result.integrada(n-1,cte[1::])

  def __str__(self):
    "Devuelve un string con la representación del polinomio"
    result = []
    for i,a in enumerate(self.coeficientes):
      if i == 0:
        if a != 0:
          result.append('{}'.format(a))
      elif i == 1:
        if a != 0:
          result.append('{:+}*x'.format(a))
      else:
        if a != 0:
          result.append('{:+}*x^{}'.format(a,i))
    return ''.join(result)

  def from_string(self, s, var='x'):
    """
    Keyword Arguments:
    s   -- Representación del polinomio como string
    var -- (default 'x') Variable del polinomio: P(var)

    Modo de uso:
    >>> P = Polinomio()
    >>> P.from_string('-x - 2 x^2 + 3x + 1 + x^4', var='x')

    No devuelve nada.
    Nota: Si una potencia aparece más de una vez, sus coeficientes se suman
    """
    sumas = s.split('+')
    if len(sumas) == 1:
      restas = s.split('-')
      if len(restas) == 1 or (len(restas)==2 and restas[0]==''):  #  si es un monomio o un binomio del estilo '0-a*x^n'
        var_split = s.split(var)
        a = ''.join(var_split[0].split()) # se asume que la constante siempre esta a la izquierda de 'x'
        if len(var_split) == 1:# es un termino independiente, n = 0
          if a == '':
            a = 0
          n = 0
        elif len(var_split) == 2:
          if a == '':
            a = 1
          elif a == '-':
            a = -1
          power_split = s.split('^')
          if len(power_split) == 1: # es un termino lineal, n = 1
            n = 1
          elif len(power_split) == 2: # es un termino n
            n = int(''.join(power_split[1].split()))
          else:
            print('ERROR: mas de un ^ por termino')
        else:
          print('ERROR: mas de una x por termino')
        a = float(a)
        self.coeficientes = [0]*n+[a]
      else:
        for i,a in enumerate(restas):
          A = Polinomio()
          if i == 0:
            A.from_string(a,var)              # el primero suma ( si empieza con resta '-1-x' se toma '0-1-x')
          else:
            A.from_string('-'+a,var)          # los siguientes restan
          self.coeficientes = self.suma_pol(A).coeficientes
    else:
      for a in sumas:
        A = Polinomio()
        A.from_string(a,var)
        self.coeficientes = self.suma_pol(A).coeficientes  # se suman termino a termino y se vuelve recursiva hasta encontrar un monomio


if __name__ == '__main__':

  print('Gaston Michel')

  P1 = Polinomio([1, 2.1, 3, 1.])   # 1 + 2.1x + 3 x^2 + x^3
  P2 = Polinomio([0, 1, 0, -1, -2])  # x - x^3 - 2x^4

  print(P1.get_coeficientes())
  print(P1.suma_pol(P2).get_coeficientes())
  P11 = P1.derivada()
  print(P11.get_coeficientes())
  P21 = P2.derivada()
  print(P21.get_coeficientes())
  P23 = P2.derivada(n=3)
  print(P23.get_coeficientes())
  print(P1)

  P3 = Polinomio()
  P3.from_string('x + 1 - x^ 2 - 3 x ^3')
  print(P3.get_coeficientes())