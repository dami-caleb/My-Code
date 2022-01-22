from guizero import App, Text

app = App("Wanted!")

app.bg = (245, 197,186) #The arguments are the RGB values and "bg" stands for background

wanted_message = Text(app,"WANTED!!!!!")
wanted_message.font = "Times New Roman"
wanted_message.text_size = 30

wanted_message1 = Text(app,"DEAD OR ALIVE.")
wanted_message1.font = "Times New Roman"
wanted_message1.text_size = 20

app.display()
