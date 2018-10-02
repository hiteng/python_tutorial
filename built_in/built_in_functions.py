





def abs_no(x):
    print abs(x)

def all_no(x):
    print all(x)

def any_no(y):
    print any(y)

def bool_no(x):
    print bool(x)


def power_func(num, power_num=2):
    return num**power_num

    res = []
    for i in l:
        res.append(power_func(i, 2))

def chr_no(a):
    print chr(a)

def cmp_nos(a,b):
    print (cmp(a, b))

def enum_no(arg_x):
    for index,value in enumerate(arg_x):
        if value == 3:
            print "Index = ", index
            print "Value = ", value


def eval_no():

    """Out[8]: str
    eval(a)
    Out[9]: 123
    type(eval(a))
    Out[10]: int
    b = 1.23
    type(b)
    Out[12]: float
    b = "1.23"
    type(b)
    Out[14]: str
    type(eval(b))
    Out[15]: float"""



def passing_check(pass_mark):


    if pass_mark > 50:
        return True
    else:
        return False

def check_result(st_marks):

    result = filter(passing_check, st_marks)
    return result



def format_func():
    print format(97, "c")
    print format(0.8, "%")
    print format("TEXT", "<")

    gb = globals()
    print(gb)
    lo = locals()
    print(lo)

def id_val():
    print id(x)

def inp_name():
    print('Enter your name:')
    input_1 = input()
    print('Hello, ' + input_1)
    

def vowel_func(char):
    """l = [1, 2, 3]
    1 in l
    Out[3]: True
    "s" in "class"
    Out[4]: True
    d = {1: 2, 3: 4}
    3 in d
    Out[6]: True"""
    vowel_chars = ["a", "e", "i", "o", "u"]
    if char in vowel_chars:
        return True
    else:
        return False

def filter_vowel(char_list):
    return filter(vowel_func, char_list)

def even_filter(num):

    if num % 2 == 0:
        return True
    else:
        return False

def filter_even(even_list):
    return filter(even_filter, even_list)

def filter_even_lambda(even_list):
    return filter(lambda num: True if num % 2 == 0 else False, even_list)




def add(x, y):
    return x+y

def reduce_add(list_num):
    return reduce(add, list_num)






if __name__ == '__main__':

    l = [1, 2, 3, 4]
    x = [1, 2, 3, 1, 7]
    y = []
    st_marks = [48, 67, 39, 82, 90]
    even_list = [2, 5, 43, 66, 80]
    num_list = [1, 2, 3, 4, 5]

    # abs_no(-10.6473)
    # print""
    # all_no(x)
    # print""
    # any_no(y)
    # print""
    # bool_no(y)
    # print""
    # chr_no(110)
    # print""
    # cmp_nos(5, 10)
    # print""
    # enum_no(x)
    # print""
    # print passing_mark(st_marks)
    # print""
    # format_func()
    # print""
    # id_val()
    # print""
    # inp_name()
    #print map(power_func, l)
    # print filter_vowel(["d", "a", "u", "class"])
    # print check_result(st_marks)
    # print reduce_add([1,2,3,4,5])
    #print filter_even(even_list)
    print filter_even_lambda(even_list)


