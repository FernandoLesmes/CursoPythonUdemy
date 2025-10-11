#En el siguiente diccionario se encuentran capitales de los paises
#  en el mundo, debes realizar un programa que pida un pais al usuario, y muestre la 
# capital de ese pais, en dado caso el pais no este en el diccionario, se debe mostrar un mensaje 
# diciendo que ese pais no se encuentra.

diccionario = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras":
 "Tegucigalpa","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": 
 "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "Espana": "Madrid"}

pais = input('Ingrese el nombre de un pais para conocer su capital: ')
#in asegura qeu elemeto este entro del otro 
pais=pais.lower()
if pais.capitalize() in diccionario:
    print(diccionario[pais.capitalize()])
else:
    print("El pais no se encuantra en el diccionario")     


