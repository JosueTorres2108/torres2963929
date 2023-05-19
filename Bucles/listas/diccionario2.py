#2- Hacer diccionarios español ingles, ingles español de animales. Escriba funciones que permitan alimentar estos diccionarios y usarlos. Genere un menú para cada una de las 4 opciones. Alimentar cada diccionario (2 funciones)
#Usar cada diccionario (2 funciones)
#3. Codifique funciones para alamacenar en tuplas de cada diccionario todos los animales en español y en ingles respectivamente. 


def españolIngles (diccionario):
    español= {"caballo" : "house",
              "mono" : "monkey",
              "gato" : "cat",
              "conejo" : "rabbit",
              "araña" : "spider",
              "vaca" : "cow",
              "pollo" : "chicken",
              "cerdo" : "pig",
              "mariposa" : "butterfly",
              "perro" : "dog"}
    diccionario=español
    return diccionario

def inglesEspañol (diccionario):
    ingles= {"horse" : "caballo",
             "monkey" : "mono",
             "cat" : "gato",
             "spider" : "araña",
             "cow" : "vaca",
             "chicken" : "pollo",
             "pig" : "cerdo",
             "butterfly" : "mariposa",
             "dog" : "perro"}
    diccionario=ingles
    return diccionario

def updateEspañol(diccionario , x , y):
    diccionario=españolIngles(diccionario)
    while x or y !=0:
        diccionario.update({x : y})
        return diccionario
    
def updateIngles(diccionario , x , y):
    diccionario=inglesEspañol(diccionario)
    while x or y !=0:
        diccionario.update({x : y})
        return diccionario
    
español={}
ingles={}


print("1.Mostrar diccionario en Español Ingles")
print("2.Mostrar diccionario en Ingles Español")
print("3.Actualizar diccionario Español")
print("4.Actualizar diccionario Ingles")


