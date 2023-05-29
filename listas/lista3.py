import random

list=[]
resta=[]
media=[]
suma=0
tam=int (random.randint(10,20))
print(tam)
for i in range(tam):
    num=int(random.randrange(100))
    list.append(num)
    suma+=num
    
division=suma/tam
for i in range(tam):
    media.append(division)
resta = [e1 - e2 for e1, e2 in zip (list,media)]
cuadrado = [e1 ** e2 for e1 , e2 in zip (list, list)]
   

print(list)
print(suma)
print(media)
print("la suma es",resta)
print("LA SUMA ES",cuadrado)
