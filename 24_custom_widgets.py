from tkinter import *
from tkinter import ttk

# Function base Custom Widget
def create_segment(parent, label_text, button_text):
        frame = ttk.Frame(parent)
        
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure((0,1,2), weight=1, uniform='a')
        
        label = ttk.Label(frame, text=label_text)
        button = ttk.Button(frame, text=button_text)
        
        label.grid(row=0, column=0, sticky='nsew')
        button.grid(row=0, column=1, sticky='nsew')
        
        return frame
    
# Class base Custom Widget
class Segment(ttk.Frame):
    def __init__(self, parent, label_text, button_text, button2_text):
        super().__init__(master = parent)
        
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0,1,2) ,weight=1, uniform='a')
        
        label = ttk.Label(self, text=label_text)
        button = ttk.Button(self, text=button_text)
        
        label.grid(row=0, column=0, sticky='nsew')
        button.grid(row=0, column=1, sticky='nsew')
        
        self.create_sub_segment(button2_text).grid(row=0, column=2, sticky='nsew')

        self.pack(expand=True, fill='both', padx=10, pady=5)
        
    def create_sub_segment(self, button_text):
        frame = ttk.Frame(self)
        
        entry = ttk.Entry(frame)
        button = ttk.Button(frame, text=button_text)
        
        entry.pack(expand=True, fill='both')
        button.pack(expand=True, fill='both')
        
        return frame

window = Tk()
window.title("Tkinter Custom Widgets")
window.geometry("400x600")


# Widgets
Segment(window, "Label 1", "Button 1", "Exercise Button")
Segment(window, "Label 2", "Button 2", "Exercise Button")
Segment(window, "Label 3", "Button 3", "Exercise Button")
Segment(window, "Label 4", "Button 4", "Exercise Button")
Segment(window, "Label 5", "Button 5", "Exercise Button")
Segment(window, "Label 6", "Button 6", "Exercise Button")

# create_segment(window, "label 1", "Button 1").pack(expand=True, fill='both', padx=10, pady=5)
# create_segment(window, "Label 2", "Button 2").pack(expand=True, fill='both', padx=10, pady=5)
# create_segment(window, "label 3", "Button 3").pack(expand=True, fill='both', padx=10, pady=5)
# create_segment(window, "label 4", "Button 4").pack(expand=True, fill='both', padx=10, pady=5)
# create_segment(window, "label 5", "Button 5").pack(expand=True, fill='both', padx=10, pady=5)
# create_segment(window, "label 6", "Button 6").pack(expand=True, fill='both', padx=10, pady=5)

window.mainloop()