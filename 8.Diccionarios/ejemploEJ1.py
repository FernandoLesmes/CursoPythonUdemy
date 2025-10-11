# Diccionario de países y capitales
diccionario = {
    "Guatemala": "Ciudad de Guatemala",
    "El Salvador": "San Salvador",
    "Honduras": "Tegucigalpa",
    "Nicaragua": "Managua",
    "Costa Rica": "San José",
    "Panamá": "Panamá",
    "Argentina": "Buenos Aires",
    "Colombia": "Bogotá",
    "Venezuela": "Caracas",
    "España": "Madrid"
}

# Pedir al usuario que ingrese un país
pais = input('Ingrese el nombre de un país para conocer su capital: ')

# Convertir la entrada a minúsculas para la comparación
pais = pais.lower()

# Crear un nuevo diccionario con claves en minúsculas
diccionario_lower = {k.lower(): v for k, v in diccionario.items()}

# Verificar si el país está en el diccionario y mostrar la capital correspondiente
if pais in diccionario_lower:
    print(f"La capital de {pais.title()} es {diccionario_lower[pais]}.")
else:
    print("El país no se encuentra en el diccionario.")