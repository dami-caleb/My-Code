import tkinter

tk =  tkinter.Tk()
tk.title("Listbox")

listbox = tkinter.Listbox(tk)
listbox.insert(0,"hello","hi","sup")
listbox.insert(2,"see")
listbox.pack()

tk.mainloop()