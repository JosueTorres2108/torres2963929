#crear un programa con una lista, donde se llene  aleatoriamente con el modulo random
#se debe crear una funcion en este se llamara "llenar lista", tendra dos parametros los cuales son (tam y rango)
#dentro de esta funcion, se usa una variable llamada lista, que sera por composicion
import random
def llenarLista(tam,rango):
    lista=[random.randrange(rango) for i in range(tam)]    
    return lista
#se define una funcion llamada "suma lista" que tendra como parametro "lista"
#se coloca la variable con su valor en este caso 0
#se usara un ciclo for que permitira que pase por cada valor
#se retorna la variable suma
def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum
#se define una funcion llamada "promediolista" que tendra como parametro "lista"
#debera retornar "sumalista" y se divira por el tamaño de la lista
def promedioLista(lista):
    return sumaLista(lista)/len(lista)

l1=llenarLista(3,10)
print(l1)
print(sumaLista(l1))
print(round(promedioLista(l1),2))
