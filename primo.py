#Escribe un programa que se encargue de comprobar si un número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.
def primo(numero):
    divisores=0
    for i in range(1,numero+1):
        if numero%i==0:
            divisores+=1
    if divisores==2:
        return True
    else:
        return False
for i in range(1,101):
    if primo(i):
        print(i)