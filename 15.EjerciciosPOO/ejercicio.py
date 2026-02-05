#realizar un programa que coste de una clase llamada estudiante
# que tenga como atributos el nombre y la nota del alummno. definir los
#metodos para inicializar sus atributos, imprimirlos y mostrar un mensaje
#con el resultado de la nota si ha apro|

class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"El alumno {self.nombre} tiene una nota de {self.nota}")

    def main(self):
        if self.nota >= 5:
            print(f"El alumno {self.nombre} ha aprobado con una nota de {self.nota}")
        else:
            print(f"El alumno {self.nombre} ha suspendido con una nota de {self.nota}")

estudiante = Estudiante("Juan", 7)
estudiante.imprimir()
estudiante.main()

estudiante2 = Estudiante("Pedro", 4)
estudiante2.imprimir()
estudiante2.main()