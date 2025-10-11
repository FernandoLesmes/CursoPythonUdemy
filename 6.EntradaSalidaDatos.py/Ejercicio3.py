#Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas

VocalMinus = input("Ingresa una vocal en miniscula: ")

consonante = input("Ingresa una letra en mayuscula: ")

VocalMinus = VocalMinus.upper()
consonante = consonante.lower()

print ("La vocal es: ", VocalMinus, " y la consonante es: ", consonante,".")

