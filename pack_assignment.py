from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Tkinter pack Layout")
window.geometry("400x600")


label1 = ttk.Label(window, text="Label 1", background='skyblue')
label2 = ttk.Label(window, text="Label 2", background='lightgreen')
label3 = ttk.Label(window, text="Label 3", background='lightyellow')
button = ttk.Button(window, text="Button 1")


label1.pack(side='top', expand=True, fill='both', pady=10, padx=10)
label2.pack(side='left', expand=True, fill='both')
label3.pack(side='top', expand=True, fill='both')
button.pack(side='top', expand=True, fill='both')




window.mainloop()