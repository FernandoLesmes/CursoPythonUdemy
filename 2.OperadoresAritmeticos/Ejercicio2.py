'''Una jugueteria tiene mucho exito en dos de sus productos 
payasos y muñecas. Suele hacer venta por correo y la empresa 
de logistica les cobra  por peso de cada paquete, asi que deben 
calcular el peso de los payasos y muñecas  que saldran en cada paquete 
a demanda. Cada payaso pesa 112 g y cada muñeca 75g. Un cliente  frecuente pide 
la cantidad de 23 payasos y 54 muñecas, realiza un programa que muestre el peso total 
 de toda la venta'''

PesoPayaso = 112
PesoMuñeca = 75

print ((PesoPayaso * 23)+(PesoMuñeca *54))
PesoTotal = ((PesoPayaso * 23)+(PesoMuñeca *54))
print(str(PesoTotal) + "g")

print("El peso total es de:",PesoTotal)