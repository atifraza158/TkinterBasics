from tkinter import *
from tkinter import ttk
from random import randint, choice

window = Tk()
window.title("Tkinter Scrollbar")
window.geometry("600x400")


canvas = Canvas(window, bg="skyblue", scrollregion=(0,0,2000,5000))
canvas.create_line(0,0,2000,5000, fill='green', width=10)

for i in range(100):
    l = randint(0,2000)
    r = randint(0, 5000)
    t = l + randint(10, 500)
    b = r + randint(10, 500)
    color = choice(('skyblue', 'orange', 'lightgreen', 'lightblue', 'crimson'))
    
    canvas.create_rectangle(l, r, t, b, fill=color)
canvas.pack(expand=True, fill='both')

canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(-int(event.delta / 60), 'units'))

scrolbar = ttk.Scrollbar(window, orient='vertical', command=canvas.yview)
canvas.configure(yscrollcommand=scrolbar.set)
scrolbar.place(relx=1, rely=0, relheight=1, anchor='ne')

canvas.bind("<Control MouseWheel>", lambda event: canvas.xview_scroll(-int(event.delta / 60), 'units'))

horizontal_scrollbar = ttk.Scrollbar(window, orient='horizontal', command=canvas.xview)
canvas.configure(xscrollcommand=horizontal_scrollbar.set)
horizontal_scrollbar.place(relx=0, rely=1, relwidth=1, anchor='sw')


window.mainloop()