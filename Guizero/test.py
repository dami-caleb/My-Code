from email import message
from tkinter.messagebox import YESNO
from guizero import App, Window,Text,TextBox,Combo, PushButton

#def second_window():
    #pass

def credential_check():
    if ((user_name.value.lower=="caleb") and (user_password=="123")):
        window1 = Window(app,bg="brown",title= "IMT 25-21 ")
        app.hide()
        welcome_screen = Text(window1,text="Welcome Caleb 😃!")
    else:
       app.warn(title="Incorrect login credentials",text="Incorrect user name or password")
        


app = App("Main window")

window_message = Text(app,text="Kindly enter your username below👇")
user_name = TextBox(app,text="",command=None)

window_message1 = Text(app,text="Kindly enter your password below👇")
user_password = TextBox(app,text="",command=None)

submit_button = PushButton(app,text="Submit",command=credential_check)



#user_input = Combo(app,options=["Yes","No"],command=second_window,selected="No")



app.display()