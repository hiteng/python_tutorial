

class MathsOperation(object):

    pi = 3.14

    def __init__(self, num_1=None, num_2=None, radius=None):
        self.num_1 = num_1
        self.num_2 = num_2
        self.radius = radius
        self.extra = None

    def add(self):
        return self.num_1 + self.num_2

    def mul(self):
        return self.num_1 * self.num_2

    def sqr(self, num):
        return num**2

    def sqr_2ab(self):
        a_sqr = self.sqr(self.num_1)
        b_sqr = self.sqr(self.num_2)
        ab_2 = 2 * self.mul()
        return a_sqr + b_sqr + ab_2

    def cal_circle_area(self):
        r_sqr = self.sqr(self.radius)
        return MathsOperation.pi * r_sqr

if __name__ == '__main__':

    obj = MathsOperation(2,3)
    print obj.add()
    print obj.mul()

    obj_1 = MathsOperation(5, 6)
    print obj_1.add()
    print obj_1.mul()

    obj_2 = MathsOperation(2, 3)
    print obj_2.sqr_2ab()

    obj_3 = MathsOperation(radius=3)
    print obj_3.cal_circle_area()
    print obj_3.extra
    obj_3.extra = 100
    print obj_3.extra
    print obj_2.extra


