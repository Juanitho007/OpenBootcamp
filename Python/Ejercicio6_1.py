class Vehiculo():
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        return "El vehiculo es color {}, tiene {} ruedas y {} puertas".format(self.color, self.ruedas, self.puertas)


class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "El vehiculo es color {}, tiene {} ruedas , {} puertas, una velocidad maxima de {} km/h, y {} cc".format(self.color, self.ruedas, self.puertas, self.velocidad, self.cilindrada)


print(Coche("azul", 4, 4, 250, 1200))
