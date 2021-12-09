import tkinter
from tkinter import END

def add_to_list():
    listbox.insert(END, entry.get())
    entry.delete(0,END)

def remove():
    listbox.delete(listbox.curselection())

tk = tkinter.Tk()
tk.title("Library")

listbox = tkinter.Listbox(tk)
listbox.pack()

title = tkinter.Label(tk, text="Book Title:")
title.pack()

title_entry= tkinter.Entry(tk)
title_entry.pack()

pages = tkinter.Label(tk, text="Enter number of pages: ")
pages.pack()

pages_entry = tkinter.Entry(tk)
pages_entry.pack()

button = tkinter.Button(tk, text="Add Title", command=add_to_list)
button.pack()

button = tkinter.Button(tk, text="Remove Title", command=remove)
button.pack()

tkinter.mainloop()