



def element_search():
    out_list = list()
    list_1 = [1, 3, 14, 23, 36, 48, 56, 69]
    inp_num = input("Enter the number to search : ")

    for i in list_1:
        while inp_num < 36:
            print out_list.append(i)
        return out_list


print element_search()