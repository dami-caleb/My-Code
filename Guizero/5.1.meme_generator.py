from tracemalloc import start
from guizero import App, TextBox, PushButton,Text,Drawing,Combo, Slider

def draw_meme():
    meme.clear()
    meme.image(0,0,image.value)
    meme.text(20,20,top_text.value,color=top_color.value,
    font=font.value,size=font_size.value)
    meme.text(20,320,bottom_text.value,color=bottom_color.value,
    font=font.value,size=font_size.value)

memegenerator_v2 = App(title="Meme Generator version 2")

welcome_screen = Text(memegenerator_v2,text="Welcome to the meme generator version 2 🥳🥰",font="Times New Roman")
welcome_screen1 = Text(memegenerator_v2,text="We have made our app better and smater")

top_text = TextBox(memegenerator_v2,text="Enter top text here", width=20,command=draw_meme)
bottom_text = TextBox(memegenerator_v2,text="Enter bottom text here",width=20,command=draw_meme)

top_color_instruction = Text(memegenerator_v2,text="Select top text color below👇")
top_color = Combo(memegenerator_v2, options=["black","white","red","green","black","orange"],command=draw_meme,selected="black")

top_color_instruction = Text(memegenerator_v2,text="Select bottom text color below👇")
bottom_color = Combo(memegenerator_v2, options=["black","white","red","green","black","orange"],command=draw_meme,selected="green")

font_instruction = Text(memegenerator_v2,text="Select font below👇")
font = Combo(memegenerator_v2,options=["Times New Roman","Arial","Verdana","Courier","Impact"],command=draw_meme)

font_size_instruction = Text(memegenerator_v2,text="Select font size below👇")
font_size = Slider(memegenerator_v2,start=5,end=20,command=draw_meme)

meme = Drawing(memegenerator_v2,width="fill",height="fill")

#draw_meme()

image_instruction = Text(memegenerator_v2,text="Change image:")
image = Combo(memegenerator_v2,options=["avatar.gif","batman.gif","image.gif","spies.gif","trash.gif","woodpecker.gif"],command=draw_meme,selected="batman.gif")

memegenerator_v2.display()