#Sacar un numero aleatorio 1 a 100
#Pedir al usuario que intente adivinar el numero
#Es un numero pequeño
#Es mas grande

import random

clave = int(random.random()*100)
num1 = 1

while num1!=clave:
    num1 = abs(int(input("Digita el numero secreto: ")))
    if num1>clave:
        print("El numero es mas pequeño")
    elif num1<clave:
        print ("El numero es mas grande")
    else: 
        print(f"El numero es: {clave}")
