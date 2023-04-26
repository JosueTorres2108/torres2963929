#Crear un programa que solicite al usuario que digite dos numeros
#El programa debera mostrar por pantalla si los numeros sonascendentes, descendentes o iguales
#Se deben crear dos variables donde se guardaran los dos nuneros, con un input para que el usuario digite los numeros
x=input('ingrese numero')
y=input('ingrese numero')
#Se deben usar las condicionales if, elif y else
#En if usaremos la expresion que si los numeros digitados son iguales muestre al usuario "Son iguales" x==y
if x==y:
    print('son iguales')
#Si esta condicion no se cumple se debera usar elif, si x es mayor que y, si se cumple con la condicion se mostrara al usuario "Descendente"
elif x>y:
    print('descendente')
#Si no se cumplen las dos condiciones anteriores el sistema va a mostrar "Ascendente"
else:
    print('ascendente')
