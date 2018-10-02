



def inp_even_odd():
    num = input("Enter the number")
    print "The number entered is : ", num

    if num % 4 == 0:
        print "The input number is Multiple of 4 and an even number."
    elif num % 2 == 0:
        print "The input number is Even."
    else:
        print "The input number is Odd."



def inp_check():
    num = input("Enter the number")
    check = input("Enter the check")

    if num % check == 0:
        print "The input number is divisible by the input."
    else:
        print "The input number is not divisible by the input."


#inp_even_odd()
print""
inp_check()