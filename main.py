rock = '''
🪨
'''
paper = '''
📃
'''
scissors = '''
✂️
'''
import random

game_image =[rock,paper,scissors] 
user_choice=int(input("what is your choice? type 0 for ROCK,1 for PAPER and 2 for SCISSORS.\n"))
computer_choice=random.randint(0,2)
print('Computer Choice:')
print(game_image[computer_choice])
print('User Choice :')
# This below line is written to handle these type of cases right?Like if we enter 4 then whi
if user_choice >= 3 or user_choice < 0:
    print("Invalid number")
elif computer_choice == user_choice:
    print(game_image[user_choice])
    print("Draw the match")
elif user_choice==0 and computer_choice == 2:
    print(game_image[user_choice])
    print("You win")    
elif computer_choice > user_choice:
    print(game_image[user_choice])
    print("You loss")
elif user_choice== 2 and computer_choice== 0:
    print(game_image[user_choice])
    print("You loss")    
elif  user_choice > computer_choice :
    print(game_image[user_choice]) 
    print("You win")