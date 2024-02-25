from tkinter import *
from tkinter import ttk
from random import choice

window = Tk()
window.title("Tkinter Tables")
# window.geometry("700x400")

# data
first_names = ['John', 'James', 'Freek', 'Williams', 'David', 'Glenn', 'Russie', 'Shane', 'Dave',]
last_names = ['Doe', 'Smith', 'Alena', 'Taylor', 'Warner', 'Maxwell', 'Dussen', 'Watson', 'Cooley']

# Table
table = ttk.Treeview(window, columns=('first', 'last', 'email'), show='headings')
table.heading('first', text="First Name",)
table.heading('last', text="last Name",)
table.heading('email', text="Email Address",)
table.pack(fill='both', expand=True) 

# table.insert(parent='', index=0, values=('John', 'Doe', 'john@example.com'))
for i in range(100):
    first = choice(first_names)
    last = choice(last_names)
    email = f'{first}{last}@gmail.com'
    data = (first, last, email)
    table.insert(parent='', index=0, values=data)

table.insert(parent='', index=END, values=('XXXX', 'YYYY', 'ZZZZ'))

# Table(Treeview) Event....
def table_select(_):
    # print(table.selection())
    for i in table.selection():
        print(table.item(i)['values'] )
    # print(table.item(table.selection()))

def delete_entry(_):
    for i in table.selection():
        table.delete(i)
    print("Deleted")

table.bind('<<TreeviewSelect>>', table_select)
table.bind('<Delete>', delete_entry)

window.mainloop()