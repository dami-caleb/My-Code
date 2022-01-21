#Widgets are the things which appear on the GUI, such as text boxes, buttons, sliders and even plan text

#Note: All widgets go between the line of code to create the App (i.e app=App()) and "app.display"

from guizero import App, Text

my_app = App(title="Welcome screen")

welcome_message = Text(my_app, text="Welcome to the Raspberry pi GUI") 

my_app.display()
