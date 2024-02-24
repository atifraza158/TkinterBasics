from tkinter import * 
from tkinter import ttk

def print_hello():
    print("helo, ")

window = Tk()
window.title("Assignment No: 1")
window.geometry("800x500")

# entry widget
input = ttk.Entry(master=window)
input.pack()

# label widget
my_label = ttk.Label(master=window, text='my label')
my_label.pack()

# Button widget
button = ttk.Button(master=window, text="Button", command=print_hello)
button.pack()

window.mainloop()