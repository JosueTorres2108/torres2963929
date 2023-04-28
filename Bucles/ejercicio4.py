suma=0
contador=0
for i in range (1,1001):
    while suma==suma+i:
        contador=contador+i
    if suma-i==i:
        print(suma)
      