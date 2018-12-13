


def prime_check():

    num = 11
    #prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            #print i
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

    # while num > 1:
    #     for i in range(2, num):
    #         if (num % i) == 0:
    #             print(num, "is not a prime number")
    #             #print(i, "times", num // i, "is", num)
    #             yield i
    #             i += 1
    #         else:
    #             print(num, "is a prime number")


a = prime_check()
print a



