from math import sqrt

# Pedimos los valores de "a", "b" y "c"
a = int(input("Ingresa un numero para el valor de a: "))
b = int(input("Ingresa un numero para el valor de b: "))
c = int(input("Ingresa un numero para el valor de c: "))

#funcion para solucion de la formula cuadratica
try:
    #si a es diferente a 0 hace la ecuacion
    if a!=0:
        x1=(-b+sqrt((b**2)-(4*a*c)))/(2*a)
        x2=(-b-sqrt((b**2)-(4*a*c)))/(2*a)
        if x1==0 and x2==0:
            print("Solucion1: x=%4.3f"%x1)
        else:
            print("Soluciones: x1=%4.3f y x2=%4.3f"%(x1,x2))

    else: #ecuacion de primer grado
        if b!=0:
            x=-c/b
            print("Solucion : x=%4.3" % x)

        else:    
            if c!=0:
                print("La ecuacion no tiene solucion")
            else:
                print("La ecuacion tiene muchas soluciones")

except:
    print("Sin solucion, los datos introducidos nos son compatibles")

    
        


