import tkinter
from tkinter import END

def add_to_list():
    listbox.insert(END, entry.get())
    entry.delete(0,END)

def remove():
    listbox.delete(listbox.curselection())

tk = tkinter.Tk()
tk.title("TO DO List App")

listbox = tkinter.Listbox(tk)
listbox.pack()

entry= tkinter.Entry(tk)
entry.pack()

button = tkinter.Button(tk, text="Add task", command=add_to_list)
button.pack()

button = tkinter.Button(tk, text="Remove selected task", command=remove)
button.pack()

tkinter.mainloop()