from tkinter import *
from tkinter import ttk

class ListFrame(ttk.Frame):
    def __init__(self, parent, text_data, item_height):
        super().__init__()
        self.pack(expand=True, fill='both')
        
        self.text_data = text_data
        self.item_number = len(text_data)
        self.list_height = self.item_number * item_height
        

window = Tk()
window.title("Tkinter Scrollable Widgets")
window.geometry("700x400")

text_list = [('Label 1', 'Button 1'), ('Label 2', 'Button 2'), ('Label 3', "Button 3"), ('Label 1', 'Button 4')]
list_frame = ListFrame(window, text_list, 100)

# canvas = Canvas(window, background='skyblue')
# canvas.create_window((20, 50), window = ttk.Button(canvas, text="Button 1"))
# canvas.pack(expand=True, fill='both')

window.mainloop()