#Calcular el máximo de números positivos introducidos por
#teclado, sabiendo que metemos números hasta que
#introduzcamos uno negativo. El negativo no cuenta.

x=1
cont=0
sum=0

while not (x<0 and x!=0):
    x= int(input("Digita un numero: "))
    cont+=1
    sum+=x
    if not(x<0 and x!=0):
        print("Si quieres salirte digita un numero negativo")
    else:
        print("Haz salido con exito")

sum-=x

print(f"El maximo de numeros positivos son: {cont-1}")
print(f"La suma de los numeros es: {sum}")

