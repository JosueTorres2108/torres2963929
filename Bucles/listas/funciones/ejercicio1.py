#Llenar un arreglo de n elementos con números generados con la función random. N es
#ingresado por el usuario. Diseñe un menú con las siguientes operaciones.
#a. Imprimir arreglo original (El primero que se generó)
#b. Suma
#c. Promedio
#d. Mayor
#e. Menor
#f. Ordenar ascendente (No perder el arreglo original; el del punto a)
#g. Ordenar descendente (No perder el arreglo original; el del punto a)
#h. Moda
#i. Mediana
#j. Buscar. Decir si encuentra el número, en qué posición(es) está, cuantas veces está

import random
def llenarLista(tam,rango):
    lista=[random.randrange(rango) for i in range(tam)]    
    return lista

def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def promedioLista(lista):
    return sumaLista(lista)/len(lista)

def mayor(lista):
    mayor=0
    for x in lista:
        if x>mayor:
            mayor=x
    return mayor

def menor(lista):
    menor=1000000
    for x in lista:
        if x<menor:
            menor=x
    return menor        
    
def ascendente(lista):
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
                lista[i],lista[j]=lista[j],lista[i]
    return lista

def descendente(lista):
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i]<lista[j]:
                lista[i],lista[j]=lista[j],lista[i]
    return lista

def moda(lista):
    ind=0 
    for i in lista: 
     cont=0 
    for f in lista: 
        if i==f: 
             cont+=1 
        if cont>ind: 
            ind=cont 
            moda=i 
    return moda

def mediana(lista):
    if len(lista)%2==0: 
     mediana = (lista[(len(lista) // 2) - 1] + lista[len(lista) // 2]) / 2 
    else:  
     mediana=lista[(len(lista)//2)] 
    
    return mediana

def buscar(lista,x):
    indice = lista.index(x)
    if x in lista:
        print("el numero " + str(x) + " si existe en la lista y esta en la posicion {} ".format(indice))
        print("esta en la lista " + str(lista.count(x)) + " veces")
    else:                
        print("el numero " + str(x) + " no existe en la lista")

lista=llenarLista(21,100)
print(lista)
print("la suma del total de los numeros de la lista es: " + str(sumaLista(lista)))
print("el promedio total de la lista es: " + str(round(promedioLista(lista),2)))
print("el numero mayor de la lista es: " + str(mayor(lista)))
print("el numero menor de la lista es: " +str(menor(lista)))
print("Lista ordenada de forma ascendete: " +str(ascendente(lista)))
print("Lista ordenada de forma descendete: " +str(descendente(lista)))
print("la moda de la lista es: " + str(moda(lista)))
print("la mediana de la lista es: " + str(mediana(lista)))
num=int(input("Escribra el numero a buscar: "))
buscar(lista,num)


