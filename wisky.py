#msg = "hello world"
#print(msg)

#import random
#num =[5,2,3,4,5]
#random.shuffle
#print(num)

#my_list =[4,3,5,7,36,7]
#print(my_list[2:5])
#person= input("nationality?")
#if person == "french" or person == "francais":
 #   name == input("comment tu t'appelle?").title()
  #  going_to_school = input("allez-vous a l'ecole?")

#if going_to_school == "yes":
 #   print(f"bievenue chez au univelcity, {name}.")
#else:
 #   print(f"au revoir, {name}.bonne journee")
    
#else: 
#if person =="italian":
    #print("preferisci parlare italiano?")
#else:
    #print("so let's speak english")








import random
num = list(range(53,69))

random.shuffle(num)

print("You can select from the list below")
print(num)

user_choice =int(input(">"))
com_choice = random.choice(num)
if user_choice in num:
    if user_choice == com_choice:
        print("You Win")
            
        print(user_choice,com_choice)

    if user_choice > com_choice:
        print("Too High")
    else:
        print("Too Low") 
        print(f"user_choice: (com_choice)")
else:
    print("invalid input")
    