import random
import os
import re

def check_play_status():
  choices = ["Yes", "No"]
  while True:
    response = input("Do you wish to play again? (Yes or No): ")
    if not response in choices:
        print("Yes or No only")
        check_play_status()

    if response == "Yes":
        os.system("cls" if os.name == "nt" else "clear")
        return True
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("Thanks for playing!")
        exit()

def play():
   play_status = True
   while play_status:
       print(" ")
       print("Rock, Paper, Scissors - Shoot!")

       user_choice = input("Choose your weapon - [R]ock], [P]aper, or [S]cissors: ")

       if not re.match("[SRP]", user_choice):
           print(" ")
           print("Please choose a correct letter!")
           continue

       print(f"You chose: {user_choice}")

       choices = ["R", "P", "S"]
       ai_choice = random.choice(choices)

       print(f"I chose: {ai_choice}")

       if ai_choice == user_choice:
           print("Tie!")
           play_status = check_play_status()
       elif ai_choice == "R" and user_choice == "S":
           print("Rock beats scissors, I win!")
           play_status = check_play_status()
       elif ai_choice == "S" and user_choice == "P":
           print("Scissors beats paper! I win!")
           play_status = check_play_status()
       elif ai_choice == "P" and user_choice == "R":
           print("Paper beats rock, I win!")
           play_status = check_play_status()
       else:
           print("You win!\n")
           play_status = check_play_status()

if __name__ == "__main__":
   try: play()
   except(KeyboardInterrupt): 
        os.system("cls" if os.name == "nt" else "clear")        
        print("Thanks for playing!")
        exit()
