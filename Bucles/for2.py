#Solicite al usuario inicio, fin y cantidad a incrementar o decrementar según el caso. Imprima la serie
a=int(input("Digite el numero de inicio: "))
b=int(input("Digite el numero de final: "))
c=int(input("Digite el numero en la cual quieres incrementar o decrementar: "))
d=0

if b>=0:
    b+=1
if b<0:
    b-=1

for i in range(a,b,c):
    print(i)