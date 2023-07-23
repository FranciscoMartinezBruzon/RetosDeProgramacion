#Escribe una función que reciba dos palabras (String) y retorne
 # verdadero o falso (Bool) según sean o no anagramas.
 # - Un Anagrama consiste en formar una palabra reordenando TODAS
 #   las letras de otra palabra inicial.
 # - NO hace falta comprobar que ambas palabras existan.
 # - Dos palabras exactamente iguales no son anagrama.

palabra1=input("escriba la palabra: ")
palabra1=list(palabra1.lower())
palabra1.sort()
print(palabra1)
palabra2=input("escriba la palabra: ")
palabra2=list(palabra2.lower())
palabra2.sort()
print(palabra2)
if (palabra1==palabra2):
  print("es anagrama")
else:
  print("no es anagrama")
