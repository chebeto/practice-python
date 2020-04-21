import random

#Se crea la variable, la cual es una lista compuesta por 25 numeros aleatorios 
numeros = [random.randint(1, 25) for i in range(25)]
#Se crea la variable Even, dentro de ella hay una lista la cual recorre los numeros de la lista anterior
#dentro de esa lista se crea una nueva, la cual se conforma por numeros pares ya que el residual debera ser igual a 0
evens = [ numeros for numeros in numeros if numeros % 2 == 0 ]
#Se imprime la lista Evens
print(evens)