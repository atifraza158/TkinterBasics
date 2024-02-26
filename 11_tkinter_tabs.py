from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Tkinter Tabs")
window.geometry("700x400")


notebook = ttk.Notebook(window)

# tab 1
tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text="Label 1")
label2 = ttk.Label(tab1, text="Label 2")
label3 = ttk.Label(tab1, text="Label 3")
label4 = ttk.Label(tab1, text="Label 4")

label1.pack()
label2.pack()
label3.pack()
label4.pack()

# Tab 2
tab2 = ttk.Frame(notebook)
entry1 = ttk.Entry(tab2)
entry2 = ttk.Entry(tab2)
entry3 = ttk.Entry(tab2)
entry4 = ttk.Entry(tab2)

entry1.pack()
entry2.pack()
entry3.pack()
entry4.pack()

# Tab 3
tab3 = ttk.Frame(notebook)
button1 = ttk.Button(tab3, text="Button 1")
button2 = ttk.Button(tab3, text="Button 2")
label5 = ttk.Label(tab3, text="Label inside Other tab")

button1.pack()
button2.pack()
label5.pack()

notebook.add(tab1, text="All Labels")
notebook.add(tab2, text="All Entries")
notebook.add(tab3, text="Other")
notebook.pack(fill='both', expand=True)



window.mainloop()