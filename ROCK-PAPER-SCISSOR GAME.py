# self made program of rock-paper-scissors game 
import random
round_number = 1
SCORE_OF_USER = 0
SCORE_OF_COMPUTER = 0
TIES = 0
while True:
 print("Round",round_number)# this will show you each round you are playing!!!
 print(".....\U0001F3AETHIS IS ROCK PAPER SCISSOR GAME.....")
#  Let computer know your name first 
 name = input("Enter your name here:")
 print("HEY! WELCOME TO ROCK PAPER SCISSORS GAME")
 print("""
 winning Rules:
 1.paper vs Rock --> \U0001F4C4Paper will win 
 2.Rock vs Scissor --> \U0001FAA8Rock will win 
 3.Scissors vs paper --> \u2702Scissors will win""")
 print()
 print(""" choices are 
 prees 1 for \U0001FAA8Rock 
 press 2 for \U0001F4C4Paper
 press 3 for \u2702Scissors""")
 choice = int(input("enter your choice from 1-3: "))
 print()
 while choice>3 or choice<1: # choice can be greater than 3 or lesser than 1 only....
    choice = int(input("Wrong choice please choose valid input"))
# It's user's choice to choose any number between 1 to 3
 if choice == 1:
    user_choice = "\U0001FAA8Rock"
 elif choice == 2:
    user_choice ="\U0001F4C4Paper"
 else:
    user_choice="\u2702Scissors" 

 print("The Users Choice is",user_choice)
 print()
#  Now it's computer's turn to choose any number between 1 to 3 
 print("Now it is computer's turn")
 print()
 computer = random.randint(1,3)
 if computer == 1:
    comp_choice ="\U0001FAA8Rock"
 elif computer == 2:
    comp_choice ="\U0001F4C4Paper"
 else: 
    comp_choice = "\u2702Scissors"
 print("computer choice is ",comp_choice)
 print()
 if((user_choice == "\U0001F4C4Paper" and comp_choice == "\U0001FAA8Rock") or (user_choice =="\U0001FAA8Rock" and comp_choice == "\U0001F4C4Paper")):
    print("Paper wins")
    print()
    result = "\U0001F4C4Paper"
 elif((user_choice == "\u2702Scissors" and comp_choice == "\U0001FAA8Rock") or (user_choice == "\U0001FAA8Rock" and comp_choice == "\u2702Scissors")):
    print("Rock wins")
    print()
    result = "\U0001FAA8Rock"
 elif(user_choice == comp_choice):
    print("it's a tie")
    print()
    result = "tie"
 else: 
    print("Scissors wins")
    result = "\u2702Scissors"
    
 if result == "tie":
    TIES+=1
 elif result == user_choice:
    print("\u2705so we can say user wins")
    SCORE_OF_USER+=1
 else: 
    print("\u2705so we can say computer wins")
    SCORE_OF_COMPUTER+=1
 print()
 print("Scores are")
 print(name,"Scores -> ",SCORE_OF_USER)
 print("Computer Scores -> ",SCORE_OF_COMPUTER)
 print("Ties Are ->  ",TIES)
 print()
 repeat = input("do you want to play another round?\n").strip()
 if repeat=="NO"or repeat=="no":
    break
 round_number+=1
print()
print("Game over!")
print("THANK YOU") 
print()
print("FINAL SCORE\n-> USER",SCORE_OF_USER)
print("-> Computer" ,SCORE_OF_COMPUTER)
print("-> ties",TIES)
print("\U0001F3AETotal Round played" ,round_number)