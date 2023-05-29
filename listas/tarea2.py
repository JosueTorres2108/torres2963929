import random  
tam= random.randint(15,20) 
lista=[random.randrange(9) for i in range(tam)] 
x=1 
print(lista) 
print(tam) 
  
  
cont=0 
posicion=[] 
x= abs(int(input("Digita un numero de 0 a 9: "))) 
if x in lista: 
     print("El numero existe") 
else: 
     print("El numero no existe") 
for i in lista: 
     if i == x: 
         cont +=1 
         posicion.append(lista.index(i)) 
         lista.remove(i) 
         lista.insert(i,15) 
if cont>=2: 
    print(f"El numero esta repetido {cont} veces") 
    if cont==1: 
        print(f"El valor {x} esta en la posicion: {posicion} de la lista") 
    else: 
        print(f"El valor {x} esta en las posiciones: {posicion} de la lista")