def divisores (a):
    divi=[]
    for i in range(1,a+1):
        if a%i==0:
            aux=i
            divi.append(aux)
    print(f"Los numeros divisibles de {a} son: {divi}")


divisores(8)
divisores(12)
divisores(16)
divisores(20)