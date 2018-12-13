

from random import *
import string

""""
This module generates a random password every time
the function is called by taking input from the choice
of the user.
"""

def pwd_generator():

    min_char = input("Enter the minimum characters for the password: ")
    max_char = input("Enter the maximum characters for the password: ")

    pwd_char = string.lowercase + string.uppercase + string.digits + string.punctuation

    password = " ".join(choice(pwd_char) for x in range(randint(min_char, max_char)))

    print "This is the generated password : ", password



pwd_generator()