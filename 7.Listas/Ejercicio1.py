#En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

#[20, 50, "Curso", 'Python', 3.14]

lista = [20, 50, "Curso", 'Python', 3.14]

print("Estos son los valores de la lista: ", lista)

dato1 = input("Ingresa un numero para la posicion 1: ")
lista[0]=dato1

dato2 = input("Ingresa un numero para la posicion 2: ")
lista[1]=dato2

print ("Esta es la lista modificada: ",lista)
