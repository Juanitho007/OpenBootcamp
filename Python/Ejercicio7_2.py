import time

hora = time.strftime('%H')
minutos = time.strftime('%M')

if int(hora) >= 19:
    print("Ya es hora de irse a casa")
else:
    print("Faltan {} horas y {} minutos para irnos a casa".format(
        18 - int(hora), 59-int(minutos)))
