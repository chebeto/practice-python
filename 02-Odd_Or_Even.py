"""   Ask the user for a number.
  Depending on whether the number is even or odd, print out an appropriate message to the user.
  Hint: how does an even / odd number react differently when divided by 2?

Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers:
  one number to check (call it num) and one number to divide by (check). 
  If check divides evenly into num, tell that to the user. If not, print a different appropriate message. """

# Se pregunta al usuario un numero para determinar si es par, impar y multiplo de 4
numeroUsuario = int (input("Hola, vamos a determinar si tu numero es par o impar...¿Cual es?: "))
residuo = numeroUsuario % 2
multiplo4 = numeroUsuario % 4

# Condiciones basicas, si el residuo es igual a 1 es impar, si es 0 es par y si cumplen con las
# dos condiciones del ELIF, entonces es par y multiplo de 4
if residuo == 1: 
  print("El numero que introduciste es impar")
elif residuo == 0 and multiplo4 == 0:
  print("El numero que introduciste es par y multiplo de 4")
else: 
  print("El numero que introduciste es par")