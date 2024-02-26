from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Tkinter Frames")
window.geometry("700x400")

# Frame
frame = ttk.Frame(window, width=200, height=200, borderwidth=10, relief=GROOVE)
frame.pack_propagate(False)
frame.pack(side='right')

# inside Frame 
label = ttk.Label(frame, text="Label inside Frame")
label.pack()

button = ttk.Button(frame, text="Button inside Frame")
button.pack()

entry = ttk.Entry(frame)
entry.pack()

# Outside the Frame
label2 = ttk.Label(window, text="Label outside frame")
label2.pack(side='right')


window.mainloop()