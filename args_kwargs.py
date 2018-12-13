


def add(*abc):

    print abc


    return sum(abc)

print add(1,2)
print add(1,2,3)
print add(1,2,3,4)


def k_w(**args):

    print args

k_w(first=1, second=2)
    # k_w({'first': 1, 'second': 2})