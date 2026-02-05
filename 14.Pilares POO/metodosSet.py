class A():
    def __init__(self):
        self._cuenta = 0 ## atributos encapsulados 
        self._contador = 10
    @property
    def cuanta(self):
        return self._cuenta
    
    @cuanta.setter
    def cuanta(self, cuanta):
        self._cuenta = cuanta
    
    @property
    def contador(self):
        return self._contador
    
    
    @cuanta.setter
    def contador(self, contador):
        self._contador = contador


a = A()
#print(a._cuenta)
print(a._cuenta)
a.cuanta = 100
print(a._cuenta)
print(a._contador)
a.contador = 1544
print(a.contador)

