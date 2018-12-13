

def cal_sqr(num1):
    result = num1**2
    print result
    return result
#cal_sqr(1)

def mul_two_nums(num1,num2):
    result = num1*num2
    print result
    return result

#mul_two_nums(1,2)

def cal_rect(num1,num2):
    a_sqr = cal_sqr(num1)
    b_sqr = cal_sqr(num2)
    a_mul_b = mul_two_nums(num1,num2)

    result = a_sqr + b_sqr + 2*a_mul_b
    print result
    return result
#cal_rect(1,2)

def xfunc(inp_no,out_of_marks=500,out_of=100):
    print inp_no, out_of_marks, out_of

xfunc(200,700)
