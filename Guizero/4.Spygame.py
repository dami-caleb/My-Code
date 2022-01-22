from guizero import App, Text, Picture, PushButton
import random as R 

def spy_function():
	adverb = ""
	spy_colour = ['yellow','green','red']
	player_colour = R.choice(spy_colour)

	if player_colour == "yellow":
        	adverb = "crazy"
	elif player_colour == "red":
        	adverb = "deadly"
	else:
        	abverb = "dangerous"	
	
	#print("Your spy is the " + adverb + " lady in: " + player_colour )
	users_spy = "Your spy is the " + adverb + " lady in: " + player_colour
	result.value = users_spy

spy_game = App(title="Spy Game")
spy_game.bg = "#F7F3F2"

first_message = Text(spy_game, text="Welcome to the Spy Game", font="Times New Roman", size= 30)
first_picture = Picture(spy_game, image="spies.gif")

second_message = Text(spy_game, text="Click the button to find who's your spy", font="Times New Roman",size=15)

spy_button = PushButton(spy_game,spy_function,text="Tell me.")

result = Text(spy_game,text="")

spy_game.display()
