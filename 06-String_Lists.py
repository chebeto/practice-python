#Se solicita una palabra al usuario
palabra = str (input("Por favor, ingresa una palabra: "))
#Se crea la variable palindromo, la cual es la palabra del usuario al reves por lista, cuando se usa [::-1] automaticamente se invierte
palindromo = palabra[::-1]

#Se comparan las dos variables, si coinciden se imprime que es un palindromo, si no coinciden se imprime el ELSE
if palabra == palindromo:
  print ('La palabra que introduciste es un palindromo')
else:
  print ('No es un palindromo')

print(palabra)
print(palindromo)