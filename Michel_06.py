class Polinomio("Objeto padre"):

  def __init__(self, coefs=[]):
    """Crea el objeto. Si los coeficientes son proporcionados lo inicializa
    Keyword Arguments:
    coefs -- (default [])
    """
    if len(coefs)<10:
      self.coeficientes=coefs
    else:
      print('ERROR: polinomio de grado mayor que 9')

  def set_coeficientes(coefs=[]):
    """Si los coeficientes son proporcionados lo inicializa
    Keyword Arguments:
    coefs -- Una lista de coeficientes
    """
    if len(coefs)<10:
      self.coeficientes=coefs
    else:
      print('ERROR: polinomio de grado mayor que 9')

  def grado():
    "Devuelve el grado del polinomio (un entero)"
    return len(self.coeficientes)-1

  def get_coeficientes():
    """Devuelve los coeficientes del polinomio """
    return self.coeficientes

  def suma_pol(p1):
    """Al polinomio le suma el polinomio `p1` y devuelve un nuevo polinomio
    Keyword Arguments:
    p1 -- Polinomio a sumar
    """
    return Polinomio([x+y for x,y in itertools.zip_longest(self.coeficientes, p1.coeficientes, fillvalue=0)])

  def derivada(n=1):
    """Devuelve la derivada (n-ésima) del polinomio (un nuevo polinomio)
    Keyword Arguments:
    n -- (default 1) Orden de derivación

    Modo de uso:
    >>> P = Polinomio([0.1,2,3,0,1)
    >>> P1 = P.derivada()
    >>> P2 = P.derivada(n=2)
    """
    result = Polinomio([x*y for x,y in enumerate(self.coeficientes)][1::])
    if n==1:
      return result
    else:
      return result.derivada(n-1)
    

  def integrada(n=1,cte=0):
    """Devuelve la antiderivada (n-ésima) del polinomio (un nuevo polinomio)

    Keyword Arguments:
    n -- (default 1) Orden de integración
    cte -- (default 0) Constante de integración

    Modo de uso:
    >>> P = Polinomio([0.1,2,3,0,1)
    >>> P1 = P.integrada()
    >>> P2 = P.integrada(cte=1.2, n=2)
    """
    result

  def __str__(self):
    "Devuelve un string con la representación del polinomio"
    pass

  def from_string(self, s, var='x'):
    """
    Keyword Arguments:
    s   -- Representación del polinomio como string
    var -- (default 'x') Variable del polinomio: P(var)

    Modo de uso:
    >>> P = Polinomio()
    >>> P.from_string('x + 2 x^2 + 3x + 1 + x^4', var='x')

    No devuelve nada.
    Nota: Si una potencia aparece más de una vez, sus coeficientes se suman
    """
    pass


if __name__ == '__main__':

  print('Nombre Apellido')

  P1 = Polinomio([1, 2.1, 3, 1.])   # 1 + 2.1x + 3 x^2 + x^4
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
  P3.from_string('x + 1 - x^2 - 3x^3')
  print(P3.get_coeficientes())
