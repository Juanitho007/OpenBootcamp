# Esta parte del código da dos opciones, 1) crea el archivo y escribe en el, 2) añade texto a un archivo existente.

class Operaciones:

    def main(self):
        self.archivo = str(
            input('Ingrese el nombre de su archivo: '))
        self.datos = datos
        print("Operaciones frecuentes")
        print("1- Escribir un archivo nuevo")
        print(
            "2- Añadir datos a archvio existente")
        print()
        Valor = None

        while Valor != 0:

            Valor = int(input(
                "Ingrese el numero de la operación deseada: "))

            if Valor == 1:
                self.escribir()
            elif Valor == 2:
                self.anadir()
            else:
                print(
                    "El numero de operación no existe")
            break

    def escribir(self):

        f = open(self.archivo, 'w')

        for linea in self.datos:
            if not linea.endswith('\n'):
                linea = linea + '\n'
            f.write(linea)
        f.close()

    def anadir(self):

        f = open(self.archivo, 'a')

        for linea in self.datos:
            if not linea.endswith('\n'):
                linea = linea + '\n'
            f.write(linea)
        f.close()


# Aqui se ingresa el texto en forma de listas separadas por ","
datos = [
    'Nombre: Juan Manuel Nuñez de la Cruz',
    'Edad: 25 años',
    'Telefono: 9211677507']

op = Operaciones()
op.main()
