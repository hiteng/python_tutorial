




def divisor_check():
    out_list = list()
    num = input("Enter the number : ")
    if num == 0:
        return "The number cannot be divisible by 0."
    else:

        for i in range(1, num+1):
            try:
                if num % i == 0:
                    out_list.append(i)
            except ZeroDivisionError:
                print "Num cannot be divided by Zero"
                print""
    return out_list




print divisor_check()
