class Empleado:
    counter = 0
    def __init__(self , Nombre:str , Cargo:str ,Salario:int):
        self.__nombre = Nombre
        self.__cargo = Cargo
        self.__salario = Salario
        Empleado.counter += 1

    def setNombre (self , Nombre:str):
        self.__nombre = Nombre
            
    def setCargo (self , Cargo:str):
        self.__cargo = Cargo
        
    def setSalario (self , Salario:int):
        self.__salario = Salario
        
        
    def getNombre (self):
        return self.__nombre
        
    def getCargo (self):
        return self.__cargo
        
    def getSalario (self):
        return self.__salario

    def Salario_Hora (self):
        hora = self.__salario/(48*4)
        return int(hora)