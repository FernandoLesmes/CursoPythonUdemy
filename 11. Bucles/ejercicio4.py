#pedir al usuario que ingrese dos numeros, despues, 
#se debe mostrar el rango de esos 2 nuemeros, pero, solo iprimiendo los nuemros q sean impares 
 
num1 = int(input("Ingrese un nuemro: "))
num2 = int(input("Ingrese un nuemro: "))

for i in range (num1, num2+1):
    if i % 2 != 0:
        print(i)
