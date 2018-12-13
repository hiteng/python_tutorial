#Write a code to calculate the income tax with 15%

def tax_amount(x):
    result = x
    print "Salary = ", result
    return result
#tax_amount(50000)

def cal_perc(inp1,pr_value):

def cal_tax(x):
    result = x * .15
    print "Tax Deducted = ", result
    return result
#cal_tax(50000)


def income_tax(x):
    a = tax_amount(x)
    b = cal_tax(x)
    result = a - b
    print "Salary after tax = ", result
    return result
income_tax(50000)


