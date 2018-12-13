
import random


def cows_bulls():

    rand_num = random.randint(1, 2)

    num = input(" Enter a number to guess : ")

    while num == rand_num:
        break
    return rand_num




print cows_bulls()