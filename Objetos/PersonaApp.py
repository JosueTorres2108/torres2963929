from persona import *

ob1 = Persona ("Josue",1013106053)

ob1.setNombre ("Torres")

ob1.setDocumento(123456789)

print(ob1.getNombre ())
print(ob1.getDocumento ())

x = 1
while x!="0":
    x=input("Escribe un curso: ")
    if x!="0":
        ob1.Cursos(x)
        
print(ob1.ConsultarCursos ())        