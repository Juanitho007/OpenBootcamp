from pickle import *


class Vehiculo:
    marca = ""
    color = ""
    año = 0

    def __init__(self, marca, color, año):
        self.marca = marca
        self.color = color
        self.año = año

    def __str__(self):
        return f' Mi vehiculo es un {self.marca.lower()}, color {self.color.lower()} y año {self.año}.'


marca = str(
    input('Ingrese marca de su vehiculo: '))
color = str(
    input('Ingrese el color de su vehiculo: '))
año = int(
    input('Ingrese el año de su vehiculo: '))
carro = Vehiculo(marca, color, año)
print(carro)

file = open('Carro.bin', 'w+b')
dump(carro, file)
file.seek(0)
nuevoCarro = load(file)
print(nuevoCarro)
file.close()
