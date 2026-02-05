class A():
    def primera(self):
        return "ESta es la clase A"
    
class B():
    def SEGUNDA(self):
        return "ESta es la clase B"

class C(A,B):
    pass   

c = C()
print(c.primera())
print(c.SEGUNDA())