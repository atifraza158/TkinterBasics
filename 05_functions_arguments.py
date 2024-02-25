from tkinter import *
from tkinter import ttk

def button_func(entry_string):
    print("A Button was pressed")
    print(entry_string.get())

window = Tk()
window.title("Functions with arguments")
window.geometry("700x400")

entry_string = StringVar(value="test")

# widgets 
entry = ttk.Entry(window, textvariable=entry_string)
entry.pack()

button = ttk.Button(window, text="Button", command=lambda: button_func(entry_string))
button.pack()

window.mainloop()