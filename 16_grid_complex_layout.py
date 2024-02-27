from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Tkinter Grid Compex LayOut")
window.geometry("700x400")


label1 = ttk.Label(window, text='Label 1', background='skyblue')
label2 = ttk.Label(window, text='Label 2', background='orange')
label3 = ttk.Label(window, text='Label 3', background='lightgreen')
label4 = ttk.Label(window, text='Label 4', background='yellow')

button1 = ttk.Button(window, text='Button 1')
button2 = ttk.Button(window, text='Button 2')

entry = ttk.Entry(window)


# Creating Grid...
window.columnconfigure((0, 1, 2), weight=1, uniform='a')
window.columnconfigure(3, weight=3, uniform='a')
window.rowconfigure(0, weight=1, uniform='a')
window.rowconfigure(1, weight=1, uniform='a')
window.rowconfigure(2, weight=1, uniform='a')
window.rowconfigure(3, weight=3, uniform='a')


# Display Labels
label1.grid(row=0, column=0, sticky='nsew')
label2.grid(row=1, column=1, rowspan=3, sticky='nsew')
label3.grid(row=1, column=0, sticky='nsew', columnspan=3, padx=20, pady=10)
label4.grid(row=3, column=3, sticky='es')

button1.grid(row=0, column=3, sticky='nsew')
button2.grid(row=2, column=2, sticky='nsew')

entry.grid(row=3, column=3, sticky='ew')


window.mainloop()