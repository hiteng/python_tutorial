

from copy import deepcopy

"""
This module includes all the functions related to lists.
"""

def list_iteration(list_arg):
    for i in list_arg:
        if i == 3:
            print i
            break


def list_iteration_enumerate(list_arg):

    for index,value in enumerate(list_arg):
        if value == 3:
            print "Length of the list: ", len(list_arg)
            print "Found element: ", value
            print "Found element at index: ", index
            break

def editing_list(list_arg):

    list_arg.append(100)
    print"list_arg: ", list_arg
    print ""
#use all the functions

def extend_list(list_arg,list_arg1):
    list_arg.extend(list_arg1)
    print "Extended list: ", list_arg
    print ""

def index_list(list_arg):


    print "Position of 4 is ", list_arg.index(4)
    print " List : ", list_arg
    print ""

    print "Inserted element ", list_arg.insert(1,7)
    print " List : ", list_arg
    print ""

    print "Pop element ", list_arg.pop()
    print "List : ", list_arg
    print ""

    print "Pop element  ", list_arg.pop(0)
    print " List : ", list_arg
    print ""

    print "Remove element 3 from the list : ", list_arg.remove(3)
    print " List : ", list_arg
    print ""

    print "Reverse the order of the list : ", list_arg.reverse()
    print " List : ", list_arg
    print ""

    print "Sort the List : ", list_arg.sort()
    print " List : ", list_arg
    print ""

    print "Count-No of occurrences  : ", list_arg.count(7)
    print " List : ", list_arg
    print ""


def list_comprehension():

    """range(10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    range(10,20)
    [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    range(10,20,2)
    [10, 12, 14, 16, 18]"""
    print ""

    print [num**2 for num in range(1, 11)]
    print [num**2 for num in range(1, 11) if num % 2 == 0]
    print [num**2 for num in range(2, 11, 2)]
    print ""

def square_num():
    output_list = list()
    for num in range(1,11):
        output_list.append(num**2)

    return output_list

def list_slicing():

    """list_1 = range(1,11)
    list_1
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_1[4]
    5
    list_1[0]
    1
    list_1[-9]
    2
    list_1[-10]
    1
    list_1[9]
    10
    list_1[-1]
    10
    """
    list_1 = range(1,11)
    print "Slicing values", list_1[0:6]
    print "Slicing values", list_1[:6]
    print "Slicing values", list_1[:]
    print "Slicing values", list_1[::2]
    print "Negative slicing", list_1[:-1]
    print "Negative slicing", list_1[-3:]
    print "Negative slicing", list_1[::-1]
    string_1 = "Google"
    print "Reverse of Google is ", string_1[::-1]


def list_extraction():
    list_1 = range(1, 11)
    output_list = list()
    print list_1
    for index,value in enumerate(list_1):
        if index < 6:
            output_list.append(value)
        else:
            break
    return output_list

def custom_reverse(arg_list):

    output_list = []
    # print "Pop element : ", list_1.pop()
    for i in range(len(arg_list)):
        #print i

        #print "Pop element : ", arg_list.pop()

        output_list.append(arg_list.pop())
    print arg_list
    return output_list





if __name__ == "__main__":
    list_1 = [1,2,3,4,5]
    list_2 = [6,7,3,9,10]

    list_iteration(list_1)
    list_iteration_enumerate(list_1)
    print list_1
    editing_list(deepcopy(list_1))
    print list_1
    extend_list(list_1,list_2)
    index_list(list_1)

    print list_comprehension.__doc__
    print list_comprehension()
    print square_num()
    print list_extraction()
    print list_slicing()
    print custom_reverse(deepcopy(list_1))
    print list_1

