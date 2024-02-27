from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Tkinter Menus")
window.geometry("700x400")

menu = Menu(window)

# File Menu Here
file_menu = Menu(menu, tearoff=False)
file_menu.add_command(label="New", command=lambda: print("New File"))
file_menu.add_command(label="Open", command=lambda: print("Open File"))


# Help Menu Here...
check_btn_str = StringVar(value="Off")

help_menu = Menu(menu, tearoff=False)
help_menu.add_command(label="Help Entries", command=lambda: print(check_btn_str.get()))
help_menu.add_checkbutton(label="Check", onvalue="On", offvalue="Off", variable=check_btn_str)


menu.add_cascade(label="File", menu=file_menu)
menu.add_cascade(label="Help", menu=help_menu)

# Exercise Menu
exercise_menu = Menu(menu, tearoff=False)
exercise_menu.add_command(label="Exercise 1", command=lambda: print("Exercise Menu"))
menu.add_cascade(label="Exercise", menu=exercise_menu)

exercise_sub_menu = Menu(menu, tearoff=False)
exercise_sub_menu.add_command(label="Some More Stuff",)
exercise_menu.add_cascade(label="More Stuff", menu=exercise_sub_menu)
window.configure(menu=menu)



# Menu Button
menu_button = ttk.Menubutton(window, text="Menu Button")
menu_button.pack()

check_btn_str2 = StringVar(value="Off")
button_sub_menu = Menu(menu_button, tearoff=False)
button_sub_menu.add_command(label="Entry 1", command=lambda: print("test 1"))
button_sub_menu.add_command(label="Entry 2", command=lambda: print(f"Checked: {check_btn_str2.get()}"))
button_sub_menu.add_checkbutton(label="Check", command=lambda: print("Checked"), onvalue="On", offvalue="Off", variable=check_btn_str2)

menu_button.configure(menu=button_sub_menu)

window.mainloop()