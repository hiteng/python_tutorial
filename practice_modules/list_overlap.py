



def list_overlap(list_arg1, list_arg2):



    return set(list_arg1).intersection(list_arg2)
    




if __name__ == '__main__':
    list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


print list_overlap(list_1, list_2)