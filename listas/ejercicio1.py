import random
tam=random.randint(15,20) 
lista=[(random.randrange(9)) for i in range (tam)]
j=1
sum=0
print(lista)

while j<=9:
    a=abs(int(input("escriba un numero de 0 a 9")))
    if a in lista:
        print("El numero existe")
    else:
        print("El numero no existe")
    for x in lista:
        if x in lista:
            sum+=1
            
        
