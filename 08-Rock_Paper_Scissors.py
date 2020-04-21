""" 
Make a two-player Rock-Paper-Scissors game.
  Ask for player plays (using input), 
  Compare them
  Print out a message of congratulations to the winner
  Ask if the players want to start a new game

Remember the rules:
  Rock beats scissors
  Scissors beats paper
  Paper beats rock 
"""

print('='*20)
print('Piedra, Papel o Tijera')
print('Las reglas ya las conoces: piedra le gana a las tijeras, tijeras al papel y papel a la piedra')
print('='*20)
print('')
#Se asingan nombre a los dos usuarios
player1 = input("[Jugador1] Cual es tu nombre? ")
player2 = input("[Jugador2] y el tuyo? ")
#Se solicita a cada usuario que introduzca su eleccion a jugar
user1_answer = input("%s, que vas a elegir? Piedra, Papel o Tijera: " % player1)
user2_answer = input("%s, y tú? cual sera tu eleccion?: " % player2)

#Se crea la funcion comparacion, la cual tiene como valores de entrada el U1 y U2
def comparacion(u1, u2):
#Se crean if para cada caso especifico
  if u1 == u2:
    return('Es un empate!')
  elif u1 == 'Piedra':
    if u2 == 'Tijera':
      return('Gana %s!' %player1)
    else:
      return('Gana %s!' %player2)
  elif u1 == 'Papel':
    if u2 == 'Piedra':
      return('Gana %s!' %player1)
    else:
      return('Gana %s!' %player2)
  elif u1 == 'Tijera':
    if u2 == 'Papel':
      return('Gana %s!' %player1)
    else:
      return('Gana %s!' %player2)

#Se manda a llamar la funcion, los valores de entrada son las elecciones de los usuarios
print(comparacion(user1_answer, user2_answer))