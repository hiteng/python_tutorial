

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

    @staticmethod
    def sqr(num):
        return num**2

    def sqr_2ab(self):
        a_sqr = self.sqr(self.num_1)
        b_sqr = self.sqr(self.num_2)
        ab_2 = 2 * self.mul()
        return a_sqr + b_sqr + ab_2



class CircleOperations(MathsOperation):

    def __init__(self, radius):

        self.radius = radius
        super(CircleOperations, self).__init__(radius=radius)

    def cal_circle_area(self):
        print self.radius
        r_sqr = self.sqr(self.radius)
        return self.pi * r_sqr

class ConeOperations(CircleOperations):
    def __init__(self, radius, height):

        self.radius = radius
        self.height = height
        super(ConeOperations, self).__init__(radius=radius)

    def cal_cone_volume(self):
        rad_sqr = self.sqr(self.radius)
        return self.pi * rad_sqr * self.height * .33

    def cal_cube_volume(self, num):
        return num**3

class CubeOperations(ConeOperations):

    def __init__(self, radius):

        self.radius = radius
        super(CubeOperations, self).__init__(radius=radius, height=None)

    def volume_cube(self):
        v_cube = self.cal_cube_volume(self.radius)
        return v_cube



if __name__ == '__main__':
    #
    obj = MathsOperation(2, 3)
    print obj.num_1
    print obj.num_2
    obj.num_3 = 100
    print obj.num_3
    # print obj.add()
    # print obj.mul()
    #
    # obj_1 = MathsOperation(5, 6)
    # print obj_1.add()
    # print obj_1.mul()
    #
    # obj_2 = MathsOperation(2, 3)
    # print obj_2.sqr_2ab()
    #
    # # obj_3 = MathsOperation(radius=3)
    # # print obj_3.cal_circle_area()
    # # print obj_3.extra
    # # obj_3.extra = 100
    # # print obj_3.extra
    # # print obj_2.extra
    #
    # obj_4 = CircleOperations(radius=2)
    # print obj_4.cal_circle_area()
    #
    obj_5 = ConeOperations(2, 3)
    print obj_5.cal_cone_volume()
    #
    # obj_6 = CubeOperations(5)
    # print obj_6.volume_cube()
    #
    # print MathsOperation.sqr(4)


