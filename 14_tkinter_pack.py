from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Tkinter Pack Method")
window.geometry("400x600")

label1 = ttk.Label(window, text="First Label", background='skyblue')
label2 = ttk.Label(window, text="Label 2", background='crimson')
label3 = ttk.Label(window, text="Third of the Label", background='green')
button = ttk.Button(window, text="Button")

# Pack Widgets
label1.pack(side='left', fill="both", expand=True)
label2.pack(side='top', expand=True, fill='both')
label3.pack(side='top', expand=True, fill='both') 
button.pack(side='top', fill='both')


window.mainloop()