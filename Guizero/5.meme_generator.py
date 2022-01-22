from guizero import App, Text, TextBox, PushButton, Drawing



meme_app = App(title="Meme Generator.")

welcome_message = Text(meme_app,text="Let's Create a meme 😃",font="Times New Roman",size=20,color="brown")

top_text = TextBox(meme_app,text="Enter top text here",width=15)
bottom_text = TextBox(meme_app,text="Enter bottom text here",width=18)

meme = Drawing(meme_app,width="fill",height="fill")

meme_app.display()

