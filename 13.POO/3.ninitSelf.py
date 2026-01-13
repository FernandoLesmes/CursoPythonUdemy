#class fabricaTelefonos():
#    marca = "Samsung"

#    def elaborarhuawei(self):
#        self.marca = "Huawei"

#telefono = fabricaTelefonos()

#telefono.elaborarhuawei()
#print (telefono.marca)

class fabricaTelefonos():
    def __init__(self, marca, color, precio, memoria, ssd):
        self.marca = marca
        self.color = color
        self.precio = precio
        self.memoria = memoria
        self.ssd = ssd

    
telefono = fabricaTelefonos('Huawei', 'Negro', 1000, 32, 128)
print (telefono.marca)
print (telefono.color)
print (telefono.precio)
print (telefono.memoria)
print (telefono.ssd)
