#banana_survey.py
"""A banana preference survey written in Python with Tkinter"""
import tkinter as tk

#we create our main window
root = tk.Tk()

#we give our window a title
root.title("Banana interest survey")

#we set the size of our root window
root.geometry('640x480+300+300')
#The resizable() method sets whether or not our window can be resized horizontally and vertically, respectively.
root.resizable(False,False)

"""Now let's start adding widgets to our survey."""
title = tk.Label(
    root,
    text = 'Please take the survey',
    font = ('Arial 16 bold'),
    bg = 'blue',
    fg = '#FF0'
)
title.pack()

#request for surveyors name
name_label = tk.Label(root, text='Kindly enter your name:')


name_inp = tk.Entry(root)


eater_inp = tk.Checkbutton(
    root,
    text = 'Check this box if you eat bananas'
    )
not_eater_inp = tk.Checkbutton(root, text="Check this box if you don't eat bananas")

#A Checkbutton creates a check box input; it includes a
#label that sits next to the box, and we can set its text using the text argument.

num_label = tk.Label(root, text='How many bananas do you eat per day?')
num_inp = tk.Spinbox(root, from_=0, to=1000, increment=1)

color_label = tk.Label(root, text='What is the best color for a banana?')

color_inp = tk.Listbox(root, height=1) #Only show selected item

#add choices
color_choices = (
'Any','Green','Green-Yellow','Yelow', 'Brown Spotted', 'Black'
)

for color in color_choices:
    color_inp.insert(tk.END, choice)

plantain_label = tk.Label(root, text='Do you eat plantain')
plantain_frame = tk.Frame(root)
plantain_yes_inp = tk.Radiobutton(plantain_frame, text='Yes')
plantain_no_inp = tk.Radiobutton(plantain_frame, text='Eww, no!')

banana_haiku_label = tk.Label(
root,
text = 'Write a haiku about bananas'
    )
banana_haiku_inp = tk.Text(root, height=3)

submit_btn = tk.Button(root, text='Submit Survey')

output_line = tk.Label(root, text='', anchor='w')

title.grid(columnspan=2)
#By default, a call to grid() will place the widget in the first column
#(column 0) of the next empty row.
name_label.grid(row=1, column=0)

name_inp.grid(row=1, column=1)

eater_inp.grid(row=2, columnspan=2, sticky='we')

num_label.grid(row=3, sticky=tk.W)
num_inp.grid(row=3, column=1, sticky=(tk.W + tk.E))

color_label.grid(row=4, columnspan=2, sticky=tk.W, pady=10)
color_inp.grid(row=5, columnspan=2, sticky=tk.W +tk.E, padx=25)
