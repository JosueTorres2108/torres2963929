import random
tam = random.randint(10,20) 
t=()
for i in range (tam):
    numero=random.randrange(100)
    t=t+(numero,)
print(t)