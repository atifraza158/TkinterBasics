from tkinter import *
from tkinter import ttk

class Window(Tk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        
        # Widgets
        self.menu = MenuFrame(self)
        
        # Run the App
        self.mainloop()
        
class MenuFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=0.3, relheight=1)
        
        self.create_widgets()
        
        
        # ttk.Label(self, background='skyblue').pack(expand=True, fill='both')
    def create_widgets(self):
        button1 = ttk.Button(self, text="Button 1")
        button2 = ttk.Button(self, text="Button 2")
        button3 = ttk.Button(self, text="Button 3")

        slider1 = ttk.Scale(self, orient='vertical')
        slider2 = ttk.Scale(self, orient='vertical')
            
        toggle_frame = ttk.Frame(self)
        menu_toggle1 = ttk.Checkbutton(toggle_frame, text='Check 1')
        menu_toggle2 = ttk.Checkbutton(toggle_frame, text='Check 2')
        
        entry = ttk.Entry(self)
            
        self.columnconfigure((0, 1, 2), weight=1, uniform='a')
        self.rowconfigure((0,1,2,3,4), weight=1, uniform='a')
            
        button1.grid(row=0, column=0, columnspan=2, sticky='nsew')
        button2.grid(row=0, column=2, sticky='nsew')
        button3.grid(row=1, column=0, columnspan=3, sticky='nsew')
        
        slider1.grid(row=2, column=0, rowspan=2, sticky='nsew', pady=10)
        slider2.grid(row=2, column=2, rowspan=2, sticky='nsew', pady=10)
        
        toggle_frame.grid(row=4, column=0, columnspan=3, sticky='nsew')
        menu_toggle1.pack(side='left', expand=True)
        menu_toggle2.pack(side='left', expand=True)
        
        entry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor='center')

Window("Class Base View", (600, 600))