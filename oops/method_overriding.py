

class MathOperation(object):

    def __init__(self):
        pass

    def sqr(self, num):
        return num**2

class ChildMathOperation(MathOperation):

    def __init__(self):
        pass

    def sqr(self, num):
        result = super(ChildMathOperation, self).sqr(num)
        return float(result)


if __name__ == '__main__':


    obj = MathOperation()
    print obj.sqr(3)

    obj_1 = ChildMathOperation()
    print obj_1.sqr(3)

