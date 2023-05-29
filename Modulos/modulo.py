from random import randint, randrange

print (randint(1,randrange (5,50)))

def randint (n1,n2):
    contador=0
    for i in range (n1,n2):
        contador+=1
        while contador ==7:
            n3=i
            return n3
        
print(randint(5,50)) 