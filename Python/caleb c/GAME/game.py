import package
from package import update_guessing_game, Update_Multiplication_Table_Caculator

print("Welcome!")
print("Which game will you like to play? 1.Guessing game 2.Multiplication table")
print("Enter respective nuber")
user_input = input()

if user_input==1:
    update_guessing_game.game()
elif user_input==2:
    Update_Multiplication_Table_Caculator.multiplication_table()
else:
    print("Wrong input")
