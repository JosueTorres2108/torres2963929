from Aprendiz import * #de la clase aprendiz importamos todos lo valores que esten en esta clase
from Curso import * #de la clase curso importamos todos los valores que esten en esta clase

objeto=Aprendiz("Ana Kurnikova",123456,'ADSO',2693629)#
#print(objeto.__dict__)
objcurso=Curso("Programacion Software","tecnico")
objeto.agregarCurso(objcurso)
#print(objeto.__dict__)
objeto.componerCurso()
objeto.componerCurso()
#print(objeto.verCursos())
for cursito in objeto.verCursos():
    print(cursito.getNombre())