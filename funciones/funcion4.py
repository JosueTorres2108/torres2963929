import random

def llenarLista(tam,rango):
    tama=random.randint(15,tam)
    lista=[round(random.uniform(1.50,rango),2) for i in range(tama)]   
    return lista

def ordenAscen(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux 
    return lista

         
def quintiles(lista,valor):
    quintile=valor*len(lista)/5
    mayor=int(quintile)
    menor=int((valor-1)*len(lista)/5)
    if len(lista)>=quintile:
        listaQuin=lista[menor:mayor]
        return listaQuin
    else: 
        return f"No se hallar el quintil"

def cuartil(lista,valor):
    cuarti=valor*len(lista)/4
    mayor=int(cuarti)
    menor=int((valor-1)*len(lista)/4)
    if len(lista)>=cuarti:
        listaCuarti=lista[menor:mayor]
        return listaCuarti
    else: 
        return f"No se hallar el cuartil"

lista1=llenarLista(100,2.00)
print(ordenAscen(lista1))
print(len(lista1))
x=1

while x!=0:
    x=abs(int(input("Digita el quintil que quieras hallar: ")))
    if x>=1 and x<=5:
        print(quintiles(lista1,x))
    j=abs(int(input("Digita el cuartil que quieras hallar: ")))
    if j>=1 and j<=4:   
        print(cuartil(lista1,j))
    elif x==0:
        print("Haz salido correctamente del programa")
    else:
        print("Este numero es invalido")
