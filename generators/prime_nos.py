


def prime_check():

    for i in range(2, 10):
            #print i
        if (i % 2) == 0:
            print(i, "is not a prime number")
            break
        else:
            print(i, "is a prime number")
    else:
        print(i, "is not a prime number")


prime_check()