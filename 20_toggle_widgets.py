from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Toggle Widgets")
window.geometry("700x400")


# For Place method.....
# def toggle_func():
#     global check_visibility
#     if check_visibility == True:
#         label1.place_forget()
#         check_visibility = False
#     else :
#         check_visibility = True
#         label1.place(relx=0.5, rely=0.5, anchor='center')


# toggle_button = ttk.Button(window, text="Toggle Button", command= toggle_func)
# toggle_button.place(x=10, y=10)

# # Label for the toggle 
# check_visibility = True
# label1 = ttk.Label(window, text="Label 1")
# label1.place(relx=0.5, rely=0.5, anchor='center')


# For Grid Method............
# def toggle_label():
#     global check_visibility
    
#     if check_visibility:
#         label1.grid_forget()
#         check_visibility = False
#     else :
#         check_visibility = True
#         label1.grid(row=0, column=1)

# window.columnconfigure((0,1), weight=1, uniform='a')
# window.rowconfigure(0, weight=1, uniform='a')


# toggle_button = ttk.Button(window, text="Toggle Button", command=toggle_label)
# toggle_button.grid(row=0, column=0)

# # Label for the toggle 
# check_visibility = True
# label1 = ttk.Label(window, text="Label 1")
# label1.grid(row=0, column=1)



# For Pack Method
def toggle_label():
    global check_visibility
    
    if check_visibility:
        label1.pack_forget()
        check_visibility = False
    else :
        check_visibility = True
        label1.pack(expand=True, fill='both')
        


# Label for the toggle 
check_visibility = True
label1 = ttk.Label(window, text="Label 1", background='skyblue')
label1.pack(expand=True, fill='both')


toggle_button = ttk.Button(window, text="Toggle Button", command=toggle_label)
toggle_button.pack(side='bottom')

window.mainloop()