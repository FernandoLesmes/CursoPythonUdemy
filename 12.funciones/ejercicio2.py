#escribir una funcion que reciba un numero entero positivo y devuelva su factorial
def factorial():
    num = int(input("Ingrese un numero entero positivo: "))
    if num > 0:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        print (factorial)   
    else:
        print ("El numero es negativo y no podemos prodeder")    

factorial()  