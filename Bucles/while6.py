#Solicitar al usuario un número de hasta 9 dígitos e
#imprimirlo en orden contrario. Ej. digito 6754 imprimo 4576
numero = 1

while numero!=0:
    numero = int(input("Ingrese un número para revertir (0 para salir): "))
    if numero == 0:
        break
    numero_revertido = int(str(numero)[::-1])
    print(numero_revertido)