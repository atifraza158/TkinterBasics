from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Pack & Frames")
window.geometry("400x600")

# Top Frame..
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame, text="Label 1", background='skyblue')
label2 = ttk.Label(top_frame, text="Second Label", background='lightgreen')

label3 = ttk.Label(window, text="Another Label", background='orange')

# Bottom Frame
bottom_frame = ttk.Frame(window)
button1 = ttk.Button(bottom_frame, text="Button 1")
label4 = ttk.Label(bottom_frame, text="Label 4", background='orange')
button2 = ttk.Button(bottom_frame, text="Button 2")

# Right Frame
right_frame = ttk.Frame(bottom_frame)

# Exercise Buttons
button3 = ttk.Button(right_frame, text="Button 3")
button4 = ttk.Button(right_frame, text="Button 4")
button5 = ttk.Button(right_frame, text="Button 5")

# Top Layout
label2.pack(side = 'left', fill='both', expand=True)
label1.pack(side = 'left', fill='both', expand=True)
top_frame.pack(expand=True, fill='both'),

# Middle Layout
label3.pack(expand=True)

# Bottom Layout
button1.pack(expand=True, side='left', fill='both')
label4.pack(expand=True, side='left', fill='both')
button2.pack(expand=True, side='left', fill='both')
bottom_frame.pack(fill='both', expand=True, padx=20, pady=20)


# Right Layout
button3.pack(expand=True, fill='both')
button4.pack(expand=True, fill='both')
button5.pack(expand=True, fill='both')
right_frame.pack(side='left',fill='both', expand=True)




window.mainloop()