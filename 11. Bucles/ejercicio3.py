#imprimir por pantallla los numeros del 1 al 10, luego pedir al usuario dos 
#numeros y mostrar el rango de numeros entre ambas cifras

for i  in range (1,11):
    print(i)

num1= int(input("Ingrese un nuemro: "));
num2= int(input("Ingrese un nuemro: "));

for i in range (num1, num2+1):
    print(i)