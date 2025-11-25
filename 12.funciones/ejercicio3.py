'''crea una funcion que pida dos numeros. Si el primero es mayor al segundo
el progrmama debe retornar el valor1; i el seguendo es mayor al primero
debe retonar -1; si ambos son iguales debe retornar 0'''


def numeros():
    num1 = float(input("Ingrese su prmer numero;"))
    num2 = float(input("Ingrese su segundo numero: "))
    if num1 > num2:
        return 1
    elif num2 > num1:
        return -1
    
    else:
        return 0
    
print(numeros())   