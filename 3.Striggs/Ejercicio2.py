#Crear un programa que tenga una variable con la cadena “Separado” y un carácter de coma (,); e inserte el carácter entre cada letra de la cadena. Ej: separar y , debería devolver s,e,p,a,r,a,r

#Pista: Debes utilizar un método de las cadenas llamado “Replace”, recuerda que la posición de los caracteres empieza en 0.

cadena = 'eparado'

palabra = "Este es el uso del metodo Replace"
print(palabra)

reemplazar =palabra.replace(" " , "*")
print(reemplazar)

reemplazar = cadena.replace("" , ",")
print("S",reemplazar)