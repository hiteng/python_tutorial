# l = 20
# b = 5
# r = 10
# a = 15
# x = 0
# print a+b
# print a*b
# print a-b
# print a/b
# print a**b
# print a%b
# print "Area of Square = ", a**2
# print "Area of Rectangle = ", l*b
# print "Area of Circle = ", 3.14*r**2


def tax_sal(salary, tax_1):
    result = salary - (salary*tax_1)
    return result

print tax_sal(50000, .15)
print ""

def st_pass(st_marks, out_of_marks):
    if st_marks > out_of_marks:
        print "Invalid marks"

    elif st_marks > 50 or st_marks < 75:
        print "Student First Class"

    elif st_marks >75 and st_marks <= 100:
        print "Student Distinction"
    else:
        print "Student failed"

st_pass(100,100)
print""

from time import sleep
for i in range(1, 100000):
    sleep(3)
    print i

