palabra = str (input("Por favor, ingresa una palabra: "))
palindromo = palabra[::-1]

if palabra == palindromo:
  print ('La palabra que introduciste es un palindromo')
else:
  print ('No es un palindromo')

print(palabra)
print(palindromo)