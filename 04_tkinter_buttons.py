from tkinter import *
from tkinter import ttk

def simple_btn(digit):
    print(f"Hello - {digit}")
    print(radio_var.get())

window = Tk()
window.title('Tkinter Buttons')
window.geometry("700x400")

# button
button = ttk.Button(master=window, text="Simple Button", command=lambda:  simple_btn(1))
button.pack()

# Check button
check_var = IntVar(value=10)
# check_var = BooleanVar(value=True)

check1 = ttk.Checkbutton(master=window, text="CheckBox 1", command=lambda: print(check_var.get()), variable=check_var, onvalue= 10, offvalue= 5)
check2 = ttk.Checkbutton(master=window, text="CheckBox 2", command=lambda: print("test"))

check1.pack()
check2.pack()

# Radio Button 
radio_var = StringVar()

radio1 = ttk.Radiobutton(master=window, text="Radio Button 1", value= 'radio 1', command=lambda: print(radio_var.get()), variable=radio_var)
radio2 = ttk.Radiobutton(master=window, text="Radio Button 2", variable=radio_var, value= 2)

radio1.pack()
radio2.pack()

# Exercise
def radio_func():
    print(check_bool.get())
    check_bool.set(False)

radio_string = StringVar()
check_bool = BooleanVar()

# Exercise 2 Radio Buttons
radio3 = ttk.Radiobutton(master=window, text="Radio A", value='A', command=radio_func, variable=radio_string)
radio4 = ttk.Radiobutton(master=window, text="Radio B", value='B', command=radio_func, variable=radio_string)

check3 = ttk.Checkbutton(master=window, text="CheckBox 3", variable=check_bool, command=lambda: print(radio_string.get()))



radio3.pack()
radio4.pack()
check3.pack()

window.mainloop()
