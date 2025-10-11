# Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”
from math import sqrt

a = int (input("Ingresa el valor de a: "))
b = int (input("Ingresa el valor de b: "))
c = int (input("Ingresa el valor de c: "))

x1 = 0
x2 = 0

if ((b**2)-(4*a*c)) < 0:
    print("No se puede realizar por q al valor negativo no podemos sacarle raz cuadrada ")
else:
    x1 = (-b + sqrt ((b**2)-(4*a*c)))/(2*a)
    x2 = (-b - sqrt ((b**2)-(4*a*c)))/(2*a) 
print( "Resultado de de X1 es: ",x1)
print( "Resultado de de X2 es: ",x2)

print("La solucion es: \nx1= ",x1, "\nx2= ",x2)