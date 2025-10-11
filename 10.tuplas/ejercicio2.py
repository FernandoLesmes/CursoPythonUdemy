#escribir una tupla que tengas las letras del alfabeto. luego debes pedir al usuario un numero, el que haya ingresado
# es la letra que debe imprimir el programa#

alfabeto = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
print(alfabeto[2])

letra = int(input("Ingrese un numero del 1 al 26: "))
print(alfabeto[letra-1])
