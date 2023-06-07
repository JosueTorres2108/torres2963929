class Curso: #se crea la clase llamada (curso)
    def __init__(self,nombre,tipo):##se inicia un constructor con dos parametros los cuales son el nombre y tipo.
        self.__nombre=nombre #se le un valor a la variable con un parametro llamado "nombre"
        self.__tipo=tipo #se le un valor a la variable con un parametro llamado "tipo"

    def getNombre(self): #aca usamos el metodo getter que se usa para retonar un valor en este caso el nombre.
        return self.__nombre