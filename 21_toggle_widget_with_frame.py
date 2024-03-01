from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Toggle Widget with Frame")
window.geometry("700x400")

def toogle_widget():
    global check_visible
    
    if check_visible:
        label1.pack_forget()
        check_visible = False
        my_frame.pack(expand=True, fill='both', before=toggle_button)
    else:
        my_frame.pack_forget()
        check_visible = True
        label1.pack(expand=True, fill='both', before=toggle_button)


check_visible = True
label1 = ttk.Label(window, text="Label Here", background="skyblue")
label1.pack(expand=True, fill='both')

toggle_button = ttk.Button(window, text="Toggle Widgets", command=toogle_widget)
toggle_button.pack()


my_frame = ttk.Frame(window)

label2 = ttk.Label(my_frame, text="Hello World")
label2.place(relx=0.5, rely=0.5, anchor='center')

entry = ttk.Entry(my_frame)
entry.place(relx=0.5, rely=0.6, anchor='center')
# my_frame.pack(expand=True, fill='both')



window.mainloop()