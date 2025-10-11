#crear un programma q tenga una lista, luego una funcion con la cual se
#van a pedir numeros al usuario para agregar a la list. debes crear una segunada 
#funcion en donde ordenen los numeros pares impares dentro de dos listas nuevas 

lista = []
num = 0
def  numero ():
    i = 0
    while i <= 5:
        num = int(input("Ingrese un numero: "))
        lista.append(num)
        i += 1

numero()
print (lista)