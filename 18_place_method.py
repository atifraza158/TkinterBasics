from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Tkinter Plce Method Layout")
window.geometry("400x600")


label1 = ttk.Label(window, text="Label 1", background='skyblue')
label2 = ttk.Label(window, text="Label 1", background='orange')
label3 = ttk.Label(window, text="Label 1", background='lightgreen')

button = ttk.Button(window, text="Button")


label1.place(x=200, y=100, width=100, height=40)
label2.place(relx=0.2, rely=0.1, relheight=0.5, relwidth=0.3)
label3.place(x = 80, y = 60, height=300, width=120)

button.place(relx=1.0, rely=1.0, anchor='se')

# Exercise label
exercise_label = ttk.Label(window, text="Center Label", background='crimson', foreground='white')
exercise_label.place(relx=0.5, rely=0.5, relwidth=0.5, height=200, anchor='center')


window.mainloop()