


def string_list():
    str_pal = input("Enter the string : ")
    print "The palindrome of the input string :", str_pal[::-1]
    print""
    if str_pal == str_pal[::-1]:
        print "The input string is a Palindrome"
    else:
        print "The input string is not a Palindrome"


string_list()


"""
      string.reverse()
"""