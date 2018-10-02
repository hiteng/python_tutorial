


def str_list_rev():

    str_1 = raw_input("Enter the strings with multiple words : ")

    spl = str_1.split()
    spl.reverse()
    result = " ".join(spl)
    return result










print str_list_rev()