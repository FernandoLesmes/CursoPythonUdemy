class A():
    def __init__(self):
        self._cuenta = 0 ## atributos encapsulados 
        self._contador = 10
    @property
    def cuanta(self):
        return self._cuenta
    
    @property
    def contador(self):
        return self._contador


a = A()
#print(a._cuenta)
print(a._cuenta)
print(a._contador)

# modificar atributos encapsulados