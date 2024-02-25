from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Tkinter Boxes")
window.geometry("700x400")


items = ('Ice Cream', 'Pizza', 'Brocolli')
food_string = StringVar(value=items[0])
combo = ttk.Combobox(window, values=items, textvariable=food_string)
combo.pack()

# combo_label = ttk.Label(window, text="Label", textvariable=food_string)
combo_label = ttk.Label(window, text="Label",)
combo_label.pack()

# SpinBox
spin = ttk.Spinbox(window, from_= 3, to=20, increment=3)
spin.pack()
spin.bind('<<Increment>>', lambda event: print("up"))
spin.bind('<<Decrement>>', lambda event: print("down"))

combo.bind('<<ComboboxSelected>>', lambda event: combo_label.config(text=f"Selected Value: {food_string.get()}"))


window.mainloop()