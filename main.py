import math
import random
print('welcome to the game')

list_of_choice= ['r', 'p', 's']         

computer_choice = random.choice (list_of_choice) 

while True:

    user_option = input ("Pick an opption from 'r', 'p', or 's' : \n")

    if user_option in list_of_choice:
        print("Player:{user_option}, CPU {computer_choice}")

        if (user_option == computer_choice):
            print("its a tie")

        elif (user_option == 'r'):
            if(computer_choice == 's'):
                print("rock beats scissors")

            else:
                print('paper beats rock')
            break            
        elif (user_option == 'p'):
            if (computer_choice == 'r'):
                print('Paper beats rock, you win!')
            else:
                print("Scissors beat paper, you lose!")
            break
        elif (user_option == 's'):
            if (computer_choice == 'p'):
                print("Scissors beat paper, you win!")
            else:
                print("Rock beat scissors, you lose!")
            break
    else:
        print("Error: try again")                    



