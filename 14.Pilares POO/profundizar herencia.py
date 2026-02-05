class animales():
    def __init__(self , nombre):
        self.nombre= nombre
       
class Perro(animales):
    def __init__(self , nombre ,sonido):
        super().__init__(nombre)
        self.sonido = sonido

perro = Perro("perro","guau")   
print(perro.sonido)    
print(perro.nombre)