'''1. En el archivo [co_nrg.dat](files/data/co_nrg.dat) se encuentran los datos de la posición de los 
máximos de un espectro de CO$_{2}$ como función del número cuántico rotacional J (entero). 
Haga un programa que lea los datos. Los ajuste con polinomios (elija el orden adecuado) y 
grafique luego los datos (con símbolos) y el ajuste con una línea sólida roja. 
Además, debe mostrar los parámetros obtenidos para el polinomio.
'''
'''2. Queremos hacer un programa que permita fitear una curva como suma de `N` funciones gaussianas:

    2.1. Haga una función, que debe tomar como argumento los arrays con los datos: `x`, `y`, y valores iniciales para las Gaussianas: 
        `fit_gaussianas(x, y, *params)` donde params son los 3N coeficientes (tres coeficientes para cada Gaussiana). 
        Debe devolver los parámetros óptimos obtenidos.
    2.2. Realice un programita que grafique los datos dados y la función que resulta de sumar las gaussianas en una misma figura.
    2.3. *Si puede* agregue líneas o flechas indicando la posición del máximo y el ancho de cada una de las Gaussianas obtenidas.
'''