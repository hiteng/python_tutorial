



def list_end(list_arg):

    out_list = list()

    x = list_arg.pop()
    out_list.insert(0, x)
    x = list_arg.pop(0)
    out_list.insert(1, x)
    print out_list









if __name__ == '__main__':

    list_1 = [14, 2, 56, 34, 22, 89, 9, 68]


list_end(list_1)