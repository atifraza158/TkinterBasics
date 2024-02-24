from tkinter import *
from tkinter import ttk

def button_func():
    # get the content of entry
    entry_text = entry.get()
    
    # Update Label
    # label.config(text=entry_text)
    # label.configure(text=entry_text)
    label['text'] = "hi, " + entry_text
    entry['state'] = 'disabled'
    
def enable_func():
    label['text'] = "Some Text"
    entry['state'] = 'enabled'

window = Tk()
window.title("Set and Get Widget Data")

label = ttk.Label(master=window, text="Some Text")
label.pack()

# Entry Widget
entry = ttk.Entry(master=window)
entry.pack()

# Button Widget
button = ttk.Button(master=window, text="Button", command=button_func)
button.pack()

# Exercise
exercise_btn = ttk.Button(master=window, text='Enable Entry', command=enable_func)
exercise_btn.pack()

window.mainloop()