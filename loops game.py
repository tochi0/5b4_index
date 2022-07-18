
import random


def guess_game(trial:int):
    Num = list(range(53,69))

random.shuffle(Num)
print("You can select from the list below")
print(Num)

user_choice =int(input(">"))
com_choice = random.choice(Num)

if user_choice in Num:
        if user_choice == com_choice:
            print("You Win")
            print(user_choice,com_choice)

if user_choice > com_choice:
    print("Too High")
else:
    print("Too Low") 
    print(f"user_choice: (com_choice)")
    
    
    trials = 3
    while trials > 0:
        
        trials =-1
    
    print("Do you want to play again? y/n")
    rematch = input(">").lower()
    
    if rematch =="y":
        print("welcome back")
        trials = 3
    else:
        print("Game Over!")    