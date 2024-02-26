from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Tkinter Frames")
window.geometry("600x400")

# Frame
frame = ttk.Frame(window, width=200,height=200, borderwidth=10, relief=GROOVE)
frame.pack_propagate(False)
frame.pack(side='left')


label = ttk.Label(frame, text="label in Frame")
label.pack()

button = ttk.Button(frame, text="Button in Frame")
button.pack()

label2 = ttk.Label(window, text="Label outside Frame")
label2.pack(side='left')

window.mainloop()