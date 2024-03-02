from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def ask_question():
    # answer = messagebox.askquestion("Title", "Would you like to close this window?")
    # answen1 = messagebox.askokcancel("Title", "Would you like to close this window?")
    # answen2 = messagebox.askyesno("Title", "Would you like to close this window?")
    answen3 = messagebox.showinfo("Info Title", "Here is Some Information")
    print(answen3)
    
# Making a Class for Create New Window
class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Extra Window")
        self.geometry('300x500')
        
        label1 = ttk.Label(self, text="Hello World").pack()
        button = ttk.Button(self, text="My Button").pack()
        label2 = ttk.Label(self, text="Label 2").pack(expand=True)
        
# Calling a Function...
def create_new_window():
    global extra_window
    extra_window = Toplevel()
    extra_window.title("Extra Window")
    extra_window.geometry('300x500')
    
    label1 = ttk.Label(extra_window, text="Hello World").pack()
    button = ttk.Button(extra_window, text="My Button").pack()
    label2 = ttk.Label(extra_window, text="Label 2").pack(expand=True)

def close_window():
    extra_window.destroy()

window = Tk()
window.title("Tkinter Multiple Windows")
window.geometry("700x400")


# new_window_btn = ttk.Button(window, text="New Window", command=create_new_window)
new_window_btn = ttk.Button(window, text="New Window", command = lambda: Extra())
new_window_btn.pack(expand=True)

close_window_btn = ttk.Button(window, text="Destroy Window", command=close_window)
close_window_btn.pack(expand=True)

ask_question_btn = ttk.Button(window, text="Dialoge Box", command=ask_question)
ask_question_btn.pack(expand=True)


window.mainloop()