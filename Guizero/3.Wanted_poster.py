from guizero import App, Text

app = App("Wanted!")

app.bg = (245, 197,186) #The arguments are the RGB values and "bg" stands for background
wanted_message = Text(app,"WANTED!!!!! DEAD OR ALIVE!")

app.display()
