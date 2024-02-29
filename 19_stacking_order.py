from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Tkinter Stacking Order")
window.geometry("700x400")

label3 = ttk.Label(window, text="Label 1", background='lightgreen')
label2= ttk.Label(window, text="Label 2", background='orange')
label1 = ttk.Label(window, text="Label 1", background='skyblue')

button1 = ttk.Button(window, text="Button 1", command=lambda: label2.lift())
button2 = ttk.Button(window, text="Button 2", command=lambda: label2.lower())
button3 = ttk.Button(window, text="Button 3", command=lambda: label3.lift())

label1.place(x = 150, y = 100, width=150, height=150)
label2.place(x = 60, y = 140, width=200, height=200)
label3.place(x = 20, y = 200, width=200, height=200)


button1.place(relx=1, rely=1, anchor='se',)
button2.place(relx=0.9, rely=1, anchor='se')
button3.place(relx=0.8, rely=1, anchor='se')


window.mainloop()