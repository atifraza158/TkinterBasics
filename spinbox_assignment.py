from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Tkinter SpinBox")
window.geometry("700x400")

values = ('A', 'B', 'C', 'D', 'E')
spin_string = StringVar(value=values[0])
spin = ttk.Spinbox(window, values=values, textvariable=spin_string)
spin.pack()

spin.bind("<<Decrement>>", lambda event: print(spin_string.get()))

window.mainloop()