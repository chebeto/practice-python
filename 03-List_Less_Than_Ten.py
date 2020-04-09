""" Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains
only elements from the original list a that are smaller than
that number given by the user. """

# Se solicita a usuario introducir un numero que comparará a la lista
criterio = int (input("Por favor, elige un numero entre 0 y 100: "))
lista = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newLista = []
# Se crea un FOR para comparar el numero dado por el usuario para ser comparado, si es igual o mayor, se agrega a la nueva lista
for element in lista:
  if element >= criterio:
    newLista.append(element)
print(newLista)