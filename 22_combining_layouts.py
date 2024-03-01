from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Combining All Layout Methods")
window.geometry("600x600")
window.minsize(600, 600)

menu_frame = ttk.Frame(window)
main_frame = ttk.Frame(window)

menu_frame.place(x = 0, y = 0, relwidth=0.3, relheight=1)
main_frame.place(relx=0.3, y = 0, relwidth=0.7, relheight=1)

# Menu Widgets
button1 = ttk.Button(menu_frame, text="Button 1")
button2 = ttk.Button(menu_frame, text="Button 2")
button3 = ttk.Button(menu_frame, text="Button 3")

slider1 = ttk.Scale(menu_frame, orient='vertical')
slider2 = ttk.Scale(menu_frame, orient='vertical')
label1 = ttk.Label(menu_frame, text="Hello", background='skyblue')

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)

button1.grid(row=0, column=0, sticky='nsew')
label1.grid(row=3, column=2, sticky='nsew')

# label1 = ttk.Label(menu_frame, text="Hello", background='skyblue').pack(fill='both', expand=True)
# label2 = ttk.Label(main_frame, text="Hello", background='lightgreen').pack(fill='both', expand=True)



window.mainloop()