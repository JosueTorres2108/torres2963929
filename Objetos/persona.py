class Persona:
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento
        self.__cursos=[]
        
    def setNombre(self,nombre):
        self.__nombre=nombre
    
    def setDocumento(self,documento):
        self.__documento=documento
    
    def Cursos(self,cursos):
        if cursos not in self.__cursos:
            self.__cursos.append(cursos)
            return self.__cursos
        
    def ConsultarCursos(self):
        return self.__cursos           
            
    def getNombre(self):
        return self.__nombre
        
    def getDocumento(self):
        return self.__documento
    
  
    