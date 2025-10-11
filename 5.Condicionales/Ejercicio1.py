
#Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal


letra = input ("Ingrese una Letra: ")

'''if letra.lower() == "a":
   print ("Es una vocal")
else: 
    if letra.lower() == "e":
        print ("Es una vocal")
    else: 
        if letra.lower() == "i":
            print ("Es una vocal")
        else:
            if letra.lower() =="o":
                print ("Es una vocal")
            else:
                if letra.lower () == "u":
                    print ("Es una vocal")
                else:
                    print ("No es vocal: ")'''

if letra.lower() in "aeiou":
    print ("Es una vocal")
else:
    print("No es una vocal")
    
# mostramos las dos maneras de obterner el resultado, tener ecuenta el in 