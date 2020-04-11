""" Take two lists and write a program that returns a list that contains
only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python """

import random

# Se generan dos listas las cuales generan 10 numeros aleatorios entre el 1 y el 25,
# en la tercer lista se iran agregando los elementos comunes de las dos listas
lista1 = [random.randint(1, 25) for i in range(10)]
lista2 = [random.randint(1, 25) for i in range(10)]
listaComumes = []

# Se ejecuta un ciclo FOR en el que se recorre cada elemento de la lista1
for element in lista1: 
  # Si el elemento de la lista2 y el elemento de la lista1 no se encuentran en la lista comun se agrega
   if element in lista2 and element not in listaComumes:
        listaComumes.append(element)

        
print(lista1)
print(lista2)
print(listaComumes)