


def fib_num():

    inp_num = input("Enter the number of Fibonacci numbers to generate : ")
    out_list = list()
    num1 = 0
    num2 = 1

    out_list.append(num1)
    out_list.append(num2)
    #print out_list
    for i in range(1, inp_num):
        num3 = num1 + num2
        out_list.append(num3)

        num1 = num2
        num2 = num3
    return out_list

def fibo_num():

    inp_num = input("Enter the number of Fibonacci numbers to generate : ")
    out_list = list()
    num1 = 0
    num2 = 1
    i = 0
    out_list.append(num1)
    out_list.append(num2)
    #print out_list
    while i < inp_num:
        num3 = num1 + num2
        out_list.append(num3)
        i += 1
        num1 = num2
        num2 = num3
    return out_list








print fibo_num()
#print fib_num()
