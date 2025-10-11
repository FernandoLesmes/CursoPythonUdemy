lista =[ 1, 2, 3]  # primer tema 
lista2 =[ 1, 2, 3]

lista3 = lista + lista2 # solo funciona la suma 
print(lista3)

# segundo tema, incorporar datos a una lista
lista = []
print(type(lista))

edad = int(input("Ingresa tu edad: "))
lista.append(edad)
print(lista)