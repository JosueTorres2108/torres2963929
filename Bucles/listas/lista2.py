import random  #Se importa un modulo llamada random

list=[]  #Se crea una variable de tipo lista, en la cual esta vacia
#Se crea una variable de tipo entero en el cual se agrega el modulo ramdom con randint. Lo que va hacer es decirle al modulo que le guarde un numero aleatorio 
# que este entre el magen del 10 y el 20
tam=int (random.randint(10,20)) 
sum=0 #Se crea una variable sum con un valor de 0
mayor=0 #Se crea una variable mayor con un valor de 0
menor=100000000 #Se crea una variable mayor con un valor de 100000000
print(tam) #Se imprime el valor que este guardado en la variable tam


#Usamos el ciclo for para indicarle que en el rango que este guardado en la variable tam
#Se debe guardar en la variable num de tipo entero un numero en un rango de 0 hasta 100
#Esos valores guardados se agregan en la varibale list que como su nombre indica es de tipo entero. Se agregan esos valores mediante el modulo "append"
#Se va guardando en la variable sum los valores de la variable num, pero antes de eso se debe sumar el valor de la variable sum y la variable num. Despues de ese procedimiento se guardan
#Si el valor de "num" es mayor que el valor de la variable "mayor" se va a guardar ese valor en la variable "Mayor"
#Si el valor de "num" es menor que el valor de la variable "menor" se va a guardar ese valor en la variable "menor"
for i in range(tam): 
    num=int(random.randrange(100))
    list.append(num)
    sum+=num
    if num>mayor: 
        mayor=num
    if num<menor and num!=0:
        menor=num

print(list) #Se imprime los valores de variable list
print(sum) #Se imprime el valor de la variable sum
print(sum/tam) #Se imprime el valor que da de la operacion de la variable sum divido entre la variable tam
print(mayor) #Se imprime el valor de la variable mayor
print(menor) #Se imprime el valor de la variable menor