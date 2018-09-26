from copy import deepcopy

def len_list(arg_list):

    len = 0

    for x in arg_list:
        len += 1
    return len


def ext_new(arg_list1,arg_list2):
    new_list = arg_list1+arg_list2
    return new_list

def del_list(arg_list):
    out_list = []
    new_list1 = arg_list[0:2]
    print arg_list
    return out_list

def list_sort(list_arg):
    new_list = list()
    for i in range(len(l3)):

        sort_num = min(l3)
        new_list.append(sort_num)
        l3.remove(sort_num)
    print new_list


if __name__ == "__main__":
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    l3 = [5,2,7,8]

    print len_list(l1)
    print ext_new(deepcopy(l1), deepcopy(l2))
    print del_list(l1)
    print list_sort(l3)
