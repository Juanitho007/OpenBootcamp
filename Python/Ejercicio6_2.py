class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):

        if self.nota >= 6:
            return str("{} muchas felicidades has aprobado, tu nota fue de {} ".format(self.nombre, self.nota))
        else:
            return str("{} lamentablemente no has aprobado, tu nota fue de {} ".format(self.nombre, self.nota))


Nombre = str(input("Ingrese su nombre: "))
Nota = float(input("Ingrese su nota: "))
print(Alumno(Nombre, Nota))
