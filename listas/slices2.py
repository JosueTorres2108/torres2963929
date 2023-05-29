import random
tam=random.randint(5,10)
lista=[random.randrange(100) for i in range(tam)]
rebanada=lista[len(lista)//2:len(lista)]
print(lista)
print(rebanada)
