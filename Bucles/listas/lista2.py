import random  

list=[]  
tam=int (random.randint(10,20)) 
sum=0 
mayor=0 
menor=100000000 
print(tam) 



num=int(random.randrange(100))
list.append(num)
sum+=num
if num>mayor: 
        mayor=num
if num<menor and num!=0:
        menor=num

print(list) 
print(sum) 
print(sum/tam) 
print(mayor) 
print(menor) 