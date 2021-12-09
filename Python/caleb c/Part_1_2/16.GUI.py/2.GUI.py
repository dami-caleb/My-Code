import tkinter
from tkinter import END

tk =  tkinter.Tk()
tk.title("Listbox")

listbox = tkinter.Listbox(tk)
listbox.insert(0,"hello","hi","sup?")
listbox.insert(2,"sie") 
listbox.insert(END,"How are you?")
listbox.pack()
listbox.delete(2)
tk.mainloop()