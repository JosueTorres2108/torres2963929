#Llenar dos arreglos de n elementos con números generados con la función random.
#Compararlos y decir
#a. Cuál de los dos tiene la suma más alta
#b. Cuál de los dos tiene el número mayor
#c. Cuál de los dos tiene el número menor
#d. Cuál es el promedio conjunto (uniendo los dos arreglos)
#e. Sacar el promedio de cada uno y decir si está por encima o por debajo del arreglo conjunto
#f. Cuál de los dos tiene mayor cantidad de pares
#g. Cuál de los dos tiene mayor cantidad de impares

import random
def llenarLista1(tam,rango):
    lista1=[random.randrange(rango) for i in range(tam)]    
    return lista1

def llenarLista2(tam,rango):
    lista2=[random.randrange(rango) for i in range(tam)]    
    return lista2

def sumaLista1(lista1):
    sum=0
    for x in lista1:
        sum+=x
    return sum

def sumaLista2(lista2):
    sum=0
    for x in lista2:
        sum+=x
    return sum

def ascendente(lista1):
    for i in range(len(lista1)-1):
        for j in range(i+1,len(lista1)):
            if lista1[i]>lista1[j]:
                lista1[i],lista1[j]=lista1[j],lista1[i]
    return lista1
                
def ascendente(lista2):
    for i in range(len(lista2)-1):
        for j in range(i+1,len(lista2)):
            if lista2[i]>lista2[j]:
                lista2[i],lista2[j]=lista2[j],lista2[i]
    return lista2

def diferenciarsumas(lista1,lista2):
    mayor=0
    suma1=0
    for x in lista1:
        suma1+=x
    suma2=0
    
    for x in lista2:
        suma2+=x
    if suma1>suma2:
        mayor=suma1
        return mayor
    elif suma2>suma1:
        mayor=suma2
        return mayor
    else:
        return f"la suma de las dos listas son iguales" 
    
def numMayor(lista1,lista2):
        mayor1=lista1.pop(-1)
        mayor2=lista2.pop(-1)
        if mayor1>mayor2:
            return(mayor1)
        elif mayor2>mayor1:
            return(mayor2)
        else:
            return f"los numeros mayores de las listas son iguales"
        
def numMenor(lista1,lista2):
        menor1=lista1.pop(0)
        menor2=lista2.pop(0)
        if menor1<menor2:
            return(menor1)
        elif menor2<menor1:
            return(menor2)
        else:
            return f"los numeros menores de las dos listas son iguales"
        
def promedioconjunto(lista1,lista2):
    suma=0
    for x in lista1:
      suma+=x
    for x in lista2:
        suma+=x
    promedio= suma/(len(lista1)+(len(lista2)))
    return promedio
         
def promedioLista1(lista1):
    return sumaLista1(lista1)/len(lista1) 

def promedioLista2(lista2):
    return sumaLista2(lista2)/len(lista2)
       
    
lista1=llenarLista1(21,100)
print("lista 1: ",lista1)

lista2=llenarLista2(21,100)
print("lista 2: ",lista2)

print("la suma del total de los numeros de la lista 1 es: " + str(sumaLista1(lista1)))
print("la suma del total de los numeros de la lista 2 es: " + str(sumaLista2(lista2)))
print("Lista 1 ordenada de forma ascendete: " +str(ascendente(lista1)))
print("Lista 2 ordenada de forma ascendete: " +str(ascendente(lista2)))
print("la suma mayor es: " + str(diferenciarsumas(lista1,lista2)))
print("el numero mayor de las dos listas es: " + str(numMayor(lista1,lista2)))
print("el numero menor de las dos listas es: " + str(numMenor(lista1,lista2)))
print("el promedio en conjunto de las dos listas es: " + str(promedioconjunto(lista1,lista2)))
print("el promedio total de la lista 1 es: " + str(round(promedioLista1(lista1),2)))
print("el promedio total de la lista 2 es: " + str(round(promedioLista2(lista2),2)))