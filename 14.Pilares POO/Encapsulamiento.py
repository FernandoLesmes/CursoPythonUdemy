#pra encapsausar un atributo 

class A():
    def __init__(self):
        self.contador =0

    def ibncrementar(self):
        self.contador +=1

    def cunata (self):
        return self.contador    
a = A()
print(a.cunata())
a.ibncrementar()
print(a.cunata())
print(a.contador)

class B():
    def __init__(self):
        self.__contador =0

    def ibncrementar(self):
        self.__contador +=1

    def cunata (self):
        return self.__contador    
b = B()
print(a.cunata())
a.ibncrementar()
print(a.cunata())
print(a.contador)