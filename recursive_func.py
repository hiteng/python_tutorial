


# def fact_num(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact_num(n-1)
#
# if __name__ == '__main__':
#
#
#     print fact_num(5)


def sum_num(n):
    if n == 1:
        return n
    else:
        return n + sum_num(n-1)

if __name__ == '__main__':
        n = 100
        print sum_num(n)