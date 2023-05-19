def palabra (diccionario,x):
    if x in diccionario:
        return diccionario[x]
    else:
        return f"El valor {x} no existe en el diccionarrio"
    

diccion = {
    "rojo": "red",
    "azul": "blue",
    "naranja": "orange",
    "negro": "black",
    "blanco": "white",
    "amarrillo": "yellow",
    "morado": "purple",
    "rosado": "pink",
    "cafe": "brown",
    "verde": "green"
}

x= input ("Digita un color en español ")

print(palabra(diccion,x))
