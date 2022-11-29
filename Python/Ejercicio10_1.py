import tkinter as tk
from tkinter import ttk

window = tk.Tk()


def reset():
    for widget in window.winfo_children():
        if isinstance(widget, tk.Radiobutton):
            rb.set(None)


l = tk.Label(
    window, text='--Selecciona tu comida favorita--', bg='blue', fg='white', font=28)
l.grid(row=0, column=0, padx=10, pady=10, sticky=tk.N)

rb = tk.StringVar()
r1 = tk.Radiobutton(
    window, text='Papas fritas', value='1', font=22, variable=rb)
r1.grid(column=0, row=1, pady=5,
        padx=5, sticky=tk.W)
r2 = tk.Radiobutton(
    window, text='Hamburguesas', value='2', font=22, variable=rb)
r2.grid(column=0, row=2, pady=5,
        padx=5, sticky=tk.W)
r3 = tk.Radiobutton(
    window, text='Hot-dogs', value='3', font=22, variable=rb)
r3.grid(column=0, row=3, pady=5,
        padx=5, sticky=tk.W)
rb.set(0)

res = tk.Button(window, text='Reset', font=22,
                fg='red', command=lambda: reset())
res.grid(column=0, row=6, padx=10, pady=10)

window.mainloop()
