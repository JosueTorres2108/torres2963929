num=1
cont=0
suma=0
prom=0
menor=0
mayor=0
while num!=0:
    num=int(input('ingrese numero'))    
    cont=cont+1
    suma+=num

    cont+=1
    prom=suma/num
print("la suma de los numeros es:",suma)
print("el promedio de los numeros es:",prom)
print(f"el usuario ingreso{cont}numeros")
print("el numero mayor es:",cont, "numeros")
