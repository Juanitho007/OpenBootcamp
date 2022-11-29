# En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
l = tk.Label(
    window, text='--Selecciona tu comida favorita--', bg='blue', fg='white', font=35)
l.grid(row=0, column=0, padx=10, pady=10, sticky=tk.N)

lista = ['Barbacoa', 'Estofado de pollo', 'Mole de pato', 'Horneado de Cerdo', 'Carne asada', 'Bisteces entomatados', 'Cochinita', 'Pavo relleno',
         'Caldo de Res', 'Menudo', 'Higado encebollado', 'Pollo frito', 'Aguachile', 'Calamar al mojo de ajo', 'Ceviche', 'Campechana', 'Arroz a la tumbada']

lista_items = tk.StringVar(value=lista)
listbox = tk.Listbox(window, height=15, listvariable=lista_items, font=28)
listbox.grid(column=0, row=1, pady=5,
             padx=5, sticky=tk.W)

window.mainloop()
