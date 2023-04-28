a=0
a=int(input("Ingrese un numero"))
b=[]
for i in range (1,a+1):
    if a % i == 0:
        b.append(i)
print("los numeros divisores", a,"son:",b)

