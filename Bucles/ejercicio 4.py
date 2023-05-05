#Determinar cuales y cuantos números perfectos hay entre 1 y 1000?

ent=1001

for i in range(1, ent):
    b=0
    for j in range(1, (i//2)+1):
        if(i%j==0):
            b+=j
    if(b==i):
        print("%s es perfecto" %i)