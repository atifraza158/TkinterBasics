from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Tkinter Layouts")
window.geometry("700x400")

label1 = ttk.Label(window, text="Label1", background="skyblue")
label2 = ttk.Label(window, text="Label2", background="crimson")

# Pack method
# label1.pack(side='left', expand=True, fill='both')
# label2.pack(side='right', expand=True, fill='both')

# Grid method
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)
# window.columnconfigure(2, weight=2)
# window.rowconfigure(0, weight=1)
# window.rowconfigure(1, weight=1)

# label1.grid(row=0, column=1, sticky='nsew')
# label2.grid(row=1, column=1, columnspan=2, sticky='nsew')

# Place method
label1.place(x=300, y = 250 ,height=100, width=200)
label2.place(relx=0.5, rely=0.5, relwidth=1, anchor='nw')


window.mainloop()