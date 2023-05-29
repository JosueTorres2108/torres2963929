diccionario = {"rojo": "red", "azul": "blue", "verde": "green", "amarillo": "yellow", "naranja": "orange", "rosado": "pink", "blanco": "white", "negro": "black", "morado": "purple", "gris": "gray"}
colores=["rojo","azul","verde","amarillo","naranja","rosado","blanco","negro","morado","gris"]

for color in colores: 
    if color in diccionario:
        print(color, "->", diccionario[color])
        
    else: 
        print(color, "no esta en el diccionario")