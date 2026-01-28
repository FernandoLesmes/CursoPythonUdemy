class fabricatelefonos():
    def __init__(self, marca, *color, **modelos):
        self.marca = marca
        self.color = color
        self.modelos = modelos
        

telefono = fabricatelefonos("Samsung", "Negro", "Blanco", m1=500, m2=1000, m3=1500, m4=2000) 
print (telefono.marca) 
print (telefono.color)     
print (telefono.modelos)

telefono.memoria = 32


print (telefono.memoria)


