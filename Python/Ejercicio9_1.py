paises = str(input(
    "Ingrese una lista de países (separados por comas:\n"))


print(sorted(set((paises.title()).split(
    "," or "" or "_" or " "))))
