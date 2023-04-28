#Lea dos numeros. Garantice que hay uno mayor que el otro. Si no es el caso pidalos de nuevo
#Reste el menor del mayor y si el resultado lo permite reste nuevamente. Diga cuanto sobra.

x,y=1,1
resta=0
while x!=0:
    print("Si quieres salirte, escribe dos veces cero ")
    x= int(input("Digite un numero: "))
    y= int(input("Digite un numero: "))
    if x<y:
        resta=y%x
    if x>y:
        resta=x%y
    print("Lo que sobra  es: " ,resta)
print("Haz salido del sistema con exito!")
