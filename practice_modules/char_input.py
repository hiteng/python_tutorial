import datetime


def char_inp():

    name = raw_input("Enter your name : ")
    print "Your name is ", name
    age = input("Enter your age")
    print "Your age is ", age
    print""
    now = datetime.datetime.now()
    msg_copy = input("Input the number of times you want to print the message :")
    print""
    num = 0
    age_new = (now.year - age) + 100
    while num < msg_copy:
        print "You will be 100 years old in the year ", age_new
        num += 1

char_inp()


