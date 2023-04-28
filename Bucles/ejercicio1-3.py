a=0
a=int(input("Ingrese un numero"))
b=[]
contador=0
suma=0
for i in range (1,a+1):
    if a % i == 0:
        b.append(i)
        contador+=1
        suma=suma+i
        
if contador<=2:
    print("es primo")
else: 
    print("no es primo")
        
print("los numeros divisores", a,"son:",b)
print(contador)
print("es un numero perfecto",suma-a)