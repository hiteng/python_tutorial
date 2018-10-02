

class MathsOperation(object):

    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def add(self):
        return self.num_1 + self.num_2

    def mul(self):
        return self.num_1 * self.num_2

if __name__ == '__main__':

    obj = MathsOperation(2,3)
    print obj.add()
    print obj.mul()

    obj_1 = MathsOperation(5,6)
    print obj_1.add()
    print obj_1.mul()
