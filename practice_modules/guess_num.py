

import random

def guess_game():

    num = random.randint(1, 9)

    inp_num = input("Enter the number between 1 and 9 : ")

    if inp_num > 9:
        print "Enter number between 1 and 9 only"
    elif inp_num < num:
        print "The number is low"
    elif inp_num > num:
        print "The number is higher"
    else:
        print "You guessed the number correctly"


    print "The generated number : ", num


guess_game()