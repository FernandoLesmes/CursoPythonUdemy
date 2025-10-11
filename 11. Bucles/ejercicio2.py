#escribir un programa que pregunte al usuario su edad y muestre por pantalla 
# todos los años que han cumplido (desde 1 asta su edad )

edad = int(input("Ingresa tu edad: "))

i = 1
while i <= edad:
    print("Has cumplido {} años".format(i))
    i += 1