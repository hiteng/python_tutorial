



def list_less_tha_ten(list_arg):
    """
    out_list = list()

    for i in list_arg:
        if i < 10:
          out_list.append(i)
    return out_list
    """

    return [i for i in list_arg if i < 10]

def inp_list_less_tha_ten(list_arg):

    """
    out_list = list()
    inp_num = input("Enter the number : ")
    for i in list_arg:
        if i < inp_num:
            out_list.append(i)
    return out_list
    """
    inp_num = input("Enter the number : ")
    return [i for i in list_arg if i < inp_num]




if __name__ == '__main__':

    list_num = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


print list_less_tha_ten(list_num)
print inp_list_less_tha_ten(list_num)

