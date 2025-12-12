# crear un programa que tenga dos funciones, una que contenga el aarea 
# de un cuadrado con argumentos de base y altura; y la otra el area de un ciculo
# con un argumento de radio.

def areaCuadrado(base, altura):
    return base * altura

print (areaCuadrado(10 , 5))

def areaCirculo(radio):
    return 3.14 * (radio ** 2)

print (areaCirculo(5))