#from tkinter import Button
from guizero import App, Text, TextBox, PushButton, Drawing

def func():
    pass


meme_app = App(title="Meme Generator.")

def draw_meme():
    
    meme.clear()
    meme.image(0,0,"batman.gif")
    meme.text(20,20,top_text.value,color= user_input1.value,font=user_input3.value)
    meme.text(20,320,bottom_text.value,color=user_input2.value,font=user_input3.value)


welcome_message = Text(meme_app,text="Let's Create a meme 😃",font="Times New Roman",size=20)


question1 = Text(meme_app,text="Which colour do you want the top text to be in 👇?")
user_input1 = TextBox(meme_app,text="Enter color here.")
question2 = Text(meme_app,text="Which colour do you want the bottom text to be in 👇?")
user_input2 = TextBox(meme_app,text="Enter color here.")
question3 = Text(meme_app,text="Which font size do you want ? 👇")
user_input3 = TextBox(meme_app,text="Enter font size here (only numbers please😅)")
button1 = PushButton(meme_app,func,text="Submit")






top_text = TextBox(meme_app,text="Enter top text here",width=15,command=draw_meme)
bottom_text = TextBox(meme_app,text="Enter bottom text here",width=18,command=draw_meme)

meme = Drawing(meme_app,width="fill",height="fill")


#draw_meme()

meme_app.display()

