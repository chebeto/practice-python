import random

numeros = [random.randint(1, 25) for i in range(25)]
evens = [ numeros for numeros in numeros if numeros % 2 == 0 ]

print(evens)