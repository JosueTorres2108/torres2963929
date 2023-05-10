def mame(x,y):
    while x!=0 or y!=0:
        x=int(input("DIGITA UN NUMERO: "))
        y=int(input("DIGITA UN NUMERO: "))
        if x>y:
            mayor=x
            menor=y
            print(f"EL NUMERO ES MAYOR ES: {x}")
            print(f"EL NUMERO ES MENOR ES: {y}")
        else:
            mayor=y
            menor=x
            print(f"EL NUMERO ES MAYOR ES: {y}")
            print(f"EL NUMERO ES MENOR ES: {x}")

    return mame

x=1
y=1

mame(x,y)