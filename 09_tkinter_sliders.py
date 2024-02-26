from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

window = Tk()
window.title("Tkinter Sliders")
window.geometry("700x400")

# Slider
slider_var = IntVar(value=10)

slider = ttk.Scale(window, 
                   command=lambda value: print(slider_var.get()), 
                   from_=0, 
                   to_= 30, 
                   variable=slider_var, 
                   orient='horizontal',
                   length=300)
slider.pack()

# slider_label = ttk.Label(window, text=slider_var.get(),)
# slider_label.pack()

# Progressbar
progress = ttk.Progressbar(window, 
                           variable=slider_var, 
                           maximum=30,
                           length=300,
                           mode='determinate'
                           )
progress.pack()

# progress.start()

# ScrolledText
scrolled_text = scrolledtext.ScrolledText(window)
scrolled_text.pack()


window.mainloop() 