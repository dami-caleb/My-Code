import tkinter
from random import randint
from tkinter import messagebox

low =0
high = 20
rand =randint(low,high)
print(rand)


def check(guess):
    if guess < rand:
        tkinter.Label(tk,text = "Your guess is low.").pack()
    elif guess > rand:
        tkinter.Label(tk,text="Your guess is to high").pack()
    else:
        tkinter.messagebox.showinfo("WOW correct!, YOU WIN.") 





tk = tkinter.Tk()
tk.title("Guessing Game!")

label = tkinter.Label(tk, text= "Guess a number between 0 and 20")
label.pack

entry= tkinter.Entry(tk)
entry.pack()

button = tkinter.Button(tk, text="Guess", command = lambda: check(int(entry.get())))
button.pack()

tk.mainloop()


