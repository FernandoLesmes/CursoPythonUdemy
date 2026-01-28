class fabricaTelefonos:
    def __init__(self , marca , color):
        self.marca = marca
        self.color = color
        print ("Objeto  {} creado".format(self.marca))

    def __str__(self):
        return "Objeto: {}".format(self.marca)


    def __del__(self):
        print ("Objeto  {} destruido".format(self.marca))    

telefono = fabricaTelefonos('Huawei', 'Negro')       

print (telefono.marca)
print (telefono)