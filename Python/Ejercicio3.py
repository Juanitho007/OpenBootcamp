peso = float(input("Ingrese su peso en Kg: "))
estatura = float(input("Ingrese su peso en Metros: "))
imc = peso/(estatura*estatura)
print("Tu indice de masa corporal es: {:.2f}".format(imc))