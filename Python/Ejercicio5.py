def bisiesto():
    numero = int(input("Ingrese un año para saber si es bisiesto: "))
    
    if(numero % 4 == 0):
        print(f"El año {numero} si es año bisiesto")
        return
    else:
        print(f"El año {numero} no es año bisiesto")
        return

print(bisiesto())