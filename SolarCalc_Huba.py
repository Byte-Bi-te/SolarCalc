import math
from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("180x240")
window.config(background='#ADD8E6')
window.title('Solar Calculator')

def calculation():
    global A_e
    global n_e
    global G_e
    global a_e
    global C_e

    A = float(A_e.get())
    n = float(n_e.get())
    G = float(G_e.get())
    a = float(a_e.get())
    C = float(C_e.get())
    T = float(T_e.get())
    cosa = math.cos(math.radians(a))
    P = int(A*n*G*cosa*C)
    res.configure(text="P = " + str(int((P*T))) + " Вт*год")

A_e = Entry(window, width=5)
A_e.focus_set()
A_e.pack()
A_e.grid(row=1, column=2, pady=5, padx=10)

n_e = Entry(window, width=5)
n_e.focus_set()
n_e.pack
n_e.grid(row=2, column=2, pady=5, padx=10)

G_e = Entry(window, width=5)
G_e.focus_set()
G_e.pack
G_e.grid(row=3, column=2, pady=5, padx=10)

a_e = Entry(window, width=5)
a_e.focus_set()
a_e.pack
a_e.grid(row=4, column=2, pady=5, padx=10)

C_e = Entry(window, width=5)
C_e.focus_set()
C_e.pack
C_e.grid(row=5, column=2, pady=5, padx=10)

T_e = Entry(window, width=5)
T_e.focus_set()
T_e.pack
T_e.grid(row=6, column=2, pady=5, padx=10)

res = Label(window)
res.focus_set()
res.pack
res.grid(row=7, column=2, pady=5, padx=10)
res.configure(text="P = ")

calc = Button(window, command=calculation, text="Calculate!")
calc.focus_set()
calc.pack
calc.grid(row=8, column=2, pady=5, padx=10)

window.mainloop()