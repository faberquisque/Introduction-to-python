'''1. En el archivo `palabras.words.gz` hay una larga lista de palabras, en formato comprimido.
Siguiendo la idea del ejemplo dado en clases realizar un histograma de las longitudes de las palabras.
'''
'''2. Modificar el programa del ejemplo de la clase para calcular el histograma de frecuencia de letras 
en las palabras (no sólo la primera). Considere el caso insensible a la capitalización: las mayúsculas 
y minúsculas corresponden a la misma letra ('á' es lo mismo que 'Á').
'''
'''3. Utilizando el mismo archivo de palabras, Guardar todas las palabras en un array y obtener los 
índices de las palabras que tienen una dada letra (por ejemplo la letra 'j'), los índices de las 
palabras con un número dado de letras (por ejemplo 5 letras), y los índices de las palabras cuya 
tercera letra es una vocal. En cada caso, dar luego las palabras que cumplen dichas condiciones.
'''
'''4. En el archivo `colision.npy` hay una gran cantidad de datos que corresponden al resultado de una simulación. 
Los datos están organizados en trece columnas. La primera corresponde a un parámetro, mientras que las 12 
restantes corresponde a cada una de las tres componentes de la velocidad de cuatro partículas. 
Calcular y graficar:
  4.1. la distribución de ocurrencias del primer parámetro.
  4.2. la distribución de ocurrencias de energías de la tercera partícula.
  4.3. la distribución de ocurrencias de ángulos de la cuarta partícula, medido respecto al tercer eje.
  4.4. la distribución de energías de la tercera partícula cuando la cuarta partícula tiene un ángulo menor a 90 grados con el tercer eje.

  Realizar los cuatro gráficos utilizando un formato adecuado para presentación (charla o poster).
'''
'''5. Leer el archivo `colision.npy` y guardar los datos en formato texto con un encabezado adecuado. 
Usando el comando mágico `%timeit` o el módulo timeit, comparar el tiempo que tarda en leer los datos 
e imprimir el último valor utilizando el formato de texto y el formato original `npy`. 
Comparar el tamaño de los dos archivos.
'''