from tkinter import *
from tkinter import ttk

def button_function():
    print("Button was pressed ")


root = Tk()
root.title("Tkinter Window")
root.geometry('800x500')


# Create widgets

# ttk widgets...
label = ttk.Label(master=root, text="This is a test")
label.pack()

# tk Widget
my_text = Text(master=root)
my_text.pack()

# ttk Entry
entry = ttk.Entry(master=root)
entry.pack()

# ttk Button

button = ttk.Button(master=root, text="A Button", command=button_function)
button.pack()

root.mainloop()