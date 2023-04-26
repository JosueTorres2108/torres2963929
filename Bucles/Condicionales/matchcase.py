#Crear un programa que muestre las opciones de sumar, restar, multiplicar y dividir.
#El usuario debera ingresar un valor de acuerdo a las opciones
#Se crean dos variables en las cuales quedaran guardados los valores que ingrese el usuario
num1,num2=100,25
#El sistema debera mostrar las opciones de unos numeros donde servira para que se seleccione una opcion que quiera el usuario
print('1-sumar')
print('2-restar')
print('3-multiplicar')
print('4-dividir')
selector=(input('Digite la opcion'))
#Ya digitado el numero el sistema usara las palabra claves que son match y case
#Estas dos sirven para simplificar las condicionales
#La sintaxis que se usa es muy sencilla, Se escribe la palabra clave "Match" luego la variable que usaremos para que se cumplan las condiciones
#luego usaremos el case con la expresion de la condicion
#Luego se pondra el codigo sobre que va a pasar si se cumple condicion, tambien con sangria 
#Los numeros tienen  comillas simples, estas sirven para decirla al sistema que los numeros son de tipo cadena o tambien llamados tipo string
match selector:
    case '1':
        print(num1+num2)
    case '2':
        print(num1-num2)
    case '3':
        print(num1*num2)
    case '4':
        print(num1/num2)