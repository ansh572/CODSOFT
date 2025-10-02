# self made program of rock paper scissors 
import random
round_number = 1
USER_SCORE = 0
COMPUTER_SCORE = 0
TIES = 0
while True:
 print(f"\n Round{round_number}")
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
 while choice>3 or choice<1:
    choice = int(input("Wrong choice please choose valid input"))

 if choice == 1:
    user_choice = "\U0001FAA8Rock"
 elif choice == 2:
    user_choice ="\U0001F4C4Paper"
 else:
    user_choice="\u2702Scissors" 

 print("The Users Choice is",user_choice)
 print()
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
    USER_SCORE+=1
 else: 
    print("\u2705so we can say computer wins")
    COMPUTER_SCORE+=1
 print()
 print("Scores are")
 print(name,"Scores -> ",USER_SCORE)
 print("Computer Scores -> ",COMPUTER_SCORE)
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
print("FINAL SCORE\n-> USER",USER_SCORE)
print("-> Computer" ,COMPUTER_SCORE)
print("-> ties",TIES)
print("\U0001F3AETotal Round played" ,round_number)

