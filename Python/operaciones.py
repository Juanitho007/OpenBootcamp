class Operaciones:
    def __init__(self):
        self.a = float(
            input("Ingrese el primer valor: "))
        self.b = float(
            input("Ingrese el segundo valor: "))

    def menu(self):
        Valor = None
        while Valor != 7:
            print("Operaciones frecuentes")
            print("1- Sumar")
            print("2- Restar")
            print("3- Multiplicar")
            print("4- Dividir")
            print()

            Valor = int(input(
                "Ingrese el numero de la operación deseada: "))

            if Valor == 1:
                self.sumar()
            elif Valor == 2:
                self.restar()
            elif Valor == 3:
                self.multiplicar
            elif Valor == 4:
                self.dividir()
            else:
                print(
                    "El numero de operación no existe")
            break

    def sumar(self):
        sumar = self.a + self.b
        print(
            "El resultado de la suma es: ", sumar)

    def restar(self):
        restar = self.a - self.b
        print(
            "El resultado de la resta es: ", restar)

    def multiplicar(self):
        multiplicar = self.a * self.b
        print(
            "El resultado de la multiplicacion es: ", multiplicar)

    def dividir(self):
        dividir = self.a / self.b
        print(
            "El resultado de la division es: ", dividir)
