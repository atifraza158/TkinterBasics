from tkinter import *
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set("Button pressed...!")

window = Tk()
window.title("Tkinter Variables")
window.geometry('700x400')

# Tkinter String Variables
string_var = StringVar()

label = ttk.Label(master=window, text="Hello", textvariable=string_var )
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

button = Button(master=window, text="Button", command=button_func)
button.pack()


# Exercise
string_var2 = StringVar(value="test")

entry1 = ttk.Entry(master=window, textvariable=string_var2)
entry2 = ttk.Entry(master=window, textvariable=string_var2)
label2 = ttk.Label(master=window, text="Label")

entry1.pack()
entry2.pack()
label2.pack()

window.mainloop()