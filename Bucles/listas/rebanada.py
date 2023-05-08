#llenar una lista con numeros aleatorios (reales con un decimal) que representen calificaciones de un curso.
#se evalua de 0 a 5.
#el curso puede tener entre 20 y 30 aprendices. 
#hallar 
#1. saque listas nuevas para los aprobados y los reprobados (se aprueba con 3)
#2. genere listas nuevas por cada unidad. es decir, los que sacan de 0 a 1 son ungrupo, los de 1 a 2 otro grupo y asi sucesivamente 
# diga cual es el promediode los que apreuban y de los qye reprueban por separado

import random

lista=[float(random.randrange(6))for i in range(random.randint(20,30))]
suma_repro=0
print(lista)

for i in range (len(lista)):
    for j in range(i+1,len(lista)):
        if lista[i]>lista[j]:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux
print("Lista, en orden",lista)

for j in lista:
    if j==3.0:
        posicion=(lista.index(j))
    if j==2.0:
        posicion1=(lista.index(j))
    if j==4.0:
        posicion2=(lista.index(j))
unidad1=lista[:posicion1-1]
unidad2=lista[posicion1:posicion2-1]
unidad3=lista[posicion2:]
aprobado=lista[posicion:]
reprobado=lista[:posicion-1]

for i in lista:
    if i<3.0:
        suma_repro+=i
        
print("Estudiantes aprobados",aprobado)
print("Estidiantes reprobados",reprobado)
print("Unidad1",unidad1)
print("Unidad2",unidad2)
print("Unidad3",unidad3)
print("Suma",suma_repro)