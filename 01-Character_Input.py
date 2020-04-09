""" Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old. """

import datetime

# Se pregunta por el nombre del usuario y se envia un saludo
print('Hola, vamos a empezar por tu nombre...')
name = input("¿Cual es?: ")
print('Mucho gusto ' + name +'!')
# Se declara la variable EDAD como integer
edad = int(input('Ahora necesito que introduzcas tu edad: '))
# Se obtiene el año acutal mediante el import DATETIME, se obtiene el año de nacimiento y se suman 100
anioActual = datetime.datetime.now ()
anioNacimiento = anioActual.year - edad
anio100 = anioNacimiento + 100
# Se convierte el entero obtenido a string para poder ser concatenado
s = str(anio100)
print('Dependiendo de tu mes de nacimiento, en el ' + s + ' estarás cumpliendo 100 años, felicidades!')