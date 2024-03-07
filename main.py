import random

choices = ["Rock", "Paper", "Scissors"]
round_number = int(input("Enter Number of Round: "))

number_of_user_win = 0
number_of_computer_win = 0
number_of_draw = 0

for i in range(round_number):
    user_choice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))
    if user_choice > 2:
        print("Invalid input, Enter Number Between(0, 2): ")
        exit()
    else:
      print("User Choice -> ", choices[user_choice])
      
    computer_choice = random.randint(0, 2)
    print("Compuer Choice-> ", choices[computer_choice])
    
    if user_choice == 0 and computer_choice == 2:
        print("User Win")
        number_of_user_win+=1
    elif user_choice == 1 and computer_choice == 0:
        print("User Win")
        number_of_user_win+=1
    elif user_choice == 2 and computer_choice == 1:
        print("User Win")
        number_of_user_win+=1
    elif user_choice == computer_choice:
        print("Draw")
        number_of_draw+=1
    else:
        print("Computer Win")
        number_of_computer_win+=1
        
print("\n")

if number_of_user_win > number_of_computer_win:
    print("User win in round.")
elif number_of_computer_win > number_of_user_win:
    print("Computer win in round.")
else:
    print("User and Computer are draw in round.")