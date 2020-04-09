""" Create a program that asks the user for a number and then
prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that
divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.) """

# Se solicita a usuario introducir un numero
numero = int (input("Por favor, ingresa un numero: "))
# Se crea una variable la cual contendra una lista,
# dentro de esa lista se usa la funcion Range desde el numero 1 al que introdujo el usuario
rango = list(range(1,numero+1))
divisores = []
# Se crea un ciclo FOR en el cual se divide el numero de usuario entre cada elemento de dicho numero hasta el 0,
# si el residuo es 0, se agrega a la nueva lista y se imprime
for elements in rango:
  if numero % elements == 0:
    divisores.append(elements)
print(divisores) 