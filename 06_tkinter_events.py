from tkinter import *
from tkinter import ttk

def get_pos(events):
    label_string = f"X: {events.x} Y: {events.y}"
    label['text'] = label_string
    label.pack()


def selection_func(event):
    selection_str = "The Entry is Selected"
    entry_selection['text'] = selection_str
    entry_selection.pack()

def unselection_func(event):
    selection_str = ""
    entry_selection['text'] = selection_str
    entry_selection.pack()

window = Tk()
window.title("Tkinter Event Binding")
window.geometry("800x600")

# widgets
label_string = StringVar(value="Coordinates Here....")
label = ttk.Label(window, text=label_string.get())
label.pack()

text = Text(master=window)
text.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text="Button")
button.pack()

selection_str = StringVar()
entry_selection = ttk.Label(master=window, text=selection_str.get())
entry_selection.pack()

# events...
window.bind("<Alt-KeyPress-a>", lambda event: print(f"an event {event}"))
window.bind("<KeyPress>", lambda event: print(f"a Button was Pressed - ({event.char})"))

text.bind("<Motion>", get_pos)
entry.bind("<FocusIn>", selection_func)
entry.bind("<FocusOut>", unselection_func)


window.mainloop()