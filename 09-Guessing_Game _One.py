"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random

numeroMisterio = random.randint(1,9)
intentos = 0
racha = 0
numeroUsuario = ''

print('='*20)
print('Adivina el numero')
print('Facil: Adivina el numero entre el 1 y el 9, si adivinas, sumas un punto')
print('Para terminar solo escribe SALIR')
print('='*20)
print('')

while numeroUsuario != numeroMisterio or numeroUsuario != 'SALIR':
  numeroUsuario = int(input("Con que numero vas a empezar? "))
  
  if numeroUsuario == 'SALIR':
    break
    
  intentos += 1

  if numeroUsuario < numeroMisterio:
    print('Muy abajo!')
  elif numeroUsuario > numeroMisterio:
    print('Muy arriba!')
  else:
    print('Adivinaste!')
    print('Y solo te llevo ', intentos, ' intentos')