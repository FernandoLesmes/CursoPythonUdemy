diccionario = { 1 : 2 , 2 : 3 , 3 : 4 }

print(diccionario)
print(diccionario.get(2)) #trae el valor de la llave 2

diccionario.pop(3) # elimina el valor y la clave 
print(diccionario)


diccionario.clear() # borra todo el diccionario
print(diccionario)

diccionario = { 1 : 2 , 2 : 3 , 3 : 4 }
print(diccionario)
diccionario.setdefault(4 , 5) # ingresa un valor al final 
print(diccionario)

diccionario2 = {4 : 5 , 6 : 7}
diccionario.update(diccionario2) # realiza la union de dos dicionarios

print(diccionario)

diccionario.copy() # crea una copia del diccionario
print(diccionario)