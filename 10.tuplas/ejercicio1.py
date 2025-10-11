#escriba una tupla con los meses del año, luego pide al usuario  ubn numero, el que aya ingresado 
#es el mes que debe mostrar en la tupla
meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
print(meses[2])

mes = int(input("Ingrese un numero del 1 al 12: "))
print(meses[mes-1])
1