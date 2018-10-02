


def prime_check():
    # num = int(raw_input("Enter the number : "))
    # a = [x for x in range(2, num) if num % x == 0]
    # print a
    # if len(a) < 1:
    #     print"The input number is a prime number"
    # else:
    #     print"The input number is not a prime number"
        # Python program to check if the input number is prime or not

    num = 10

    # take input from the user
    # num = int(input("Enter a number: "))

    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            print i
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                break
        else:
            print(num, "is a prime number")

    # if input number is less than
    # or equal to 1, it is not prime
    else:
        print(num, "is not a prime number")


prime_check()
