"""Hello World application for TKinter"""
import tkinter as tk
root = tk.Tk()                                 
label = tk.Label(root,text="Welcome to grade caculator!")
label.pack()

welcome = tk.Label(root, text="Kindly enter your grade in the filed below")
welcome.pack()

user_input = tk.Entry(root,text="Enter grade here")
user_input.pack()

submit_button = tk.Button(root,text="Click to submit")
submit_button.pack()

root.mainloop()
