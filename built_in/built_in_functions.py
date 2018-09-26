





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

#def eval_no():

def passing_mark(pass_mark):


    if pass_mark > 50:
        return True
    else:
        return False

    result = filter(passing_mark, st_marks)

    for pass_mark in result:
        print pass_mark

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





if __name__ == '__main__':

    l = [1, 2, 3, 4]
    x = [1, 2, 3, 1, 7]
    y = []
    st_marks = [48, 67, 39, 82, 90]

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
print map(power_func, l)




