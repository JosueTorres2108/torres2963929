from Empleado import *

ob1 = Empleado ("Josue" , "Analisis" , 1500000)
ob1.setNombre ("Torres")
ob1.setCargo ("Contabilidad")
ob1.setSalario (700000)

print(ob1.getNombre())
print(ob1.getCargo())
print(ob1.getSalario())

print(ob1.Salario_Hora())