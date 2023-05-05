#Calcular la operación x n sin utilizar la función pow

import math

base = 1
exponente = 1

while base!=0:
    base = int(input("Digita el numero Base: "))
    exponente = int(input("Digita el exponente : "))
    operacion = int(math.pow (base , exponente ))

    print(f"El resultado de esa operacion es: {operacion}")


base = 1
exponente = 1

while exponente!=0:
    if base!=0:
        base = int(input("Digita el numero Base: "))
        exponente = int(input("Digita el exponente : "))
        operacion = base**exponente

    if exponente!=0:
        print(f"El resultado de esa operacion es: {operacion}")
    else:
        print("Haz salido exitosamente")