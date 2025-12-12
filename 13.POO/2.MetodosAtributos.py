class fabricaTelefonos():
    marca = "Samsung"
    color = "Negro"
    precio = 1000
    memoria = 32
    ssd = 128

    def llamar(self , mensaje):# metodos 
        return mensaje

    def escucharmusisca(self):
        print ( "Escuchando musica")

telefonos = fabricaTelefonos()

telefonos.marca
telefonos.color
telefonos.precio
telefonos.memoria
telefonos.ssd


print (telefonos.llamar("Estoy llamando"))
telefonos.escucharmusisca()
