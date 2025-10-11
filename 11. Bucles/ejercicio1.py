# escribir un progrmama que pida un numero al mismo usuario y muestre las tablas de multiplicar de ese numero 

nun = int(input("Ingrese un numero: "))
i = 0
multi = 0

while i <=10:
    multi = nun * i
    print ("{} x {} = {}".format(nun, i, multi))
    i += 1