
import unittest
import maths_class
from maths_class import MathsOperation
from maths_class import CircleOperations
from maths_class import ConeOperations
from maths_class import CubeOperations


class TestCal(unittest.TestCase):

    def test_add(self):
        res = maths_class.MathsOperation(3, 3)
        self.assertEqual(res.add(), 5)
        res1 = maths_class.MathsOperation(-1, 1)
        self.assertEquals(res1.add(), 0)
        res2 = maths_class.MathsOperation(-1, -1)
        self.assertEqual(res2.add(), -2)

    def test_mul(self):
        res3 = maths_class.MathsOperation(3, 4)
        self.assertEquals(res3.mul(), 12)
        res4 = maths_class.MathsOperation(-1, 1)
        self.assertEqual(res4.mul(), -1)
        res5 = maths_class.MathsOperation(-1, -1)
        self.assertEqual(res5.mul(), 1)

    def test_sqr(self):
        self.assertEquals(MathsOperation.sqr(3), 9)
        self.assertEqual(MathsOperation.sqr(-1), 1)
        self.assertEqual(MathsOperation.sqr(0), 0)

    def test_sqr_2ab(self):
        res6 = maths_class.MathsOperation(2, 3)
        self.assertEqual(res6.sqr_2ab(), 25)
        res7 = maths_class.MathsOperation(1, -1)
        self.assertEqual(res7.sqr_2ab(), 0)
        res8 = maths_class.MathsOperation(-1, 0)
        self.assertEqual(res8.sqr_2ab(), 1)

    def test_cal_circle_area(self):
        res9 = maths_class.CircleOperations(2)
        self.assertEqual(res9.cal_circle_area(), 12.56)
        res10 = maths_class.CircleOperations(3)
        self.assertNotEqual(res10.sqr_2ab(), 10)
        res11 = maths_class.CircleOperations(0)
        self.assertNotEqual(res11.sqr_2ab(), 1)
    #
    def test_cal_cone_vol(self):
        res12 = maths_class.ConeOperations(2, 3)
        self.assertEqual(res12.cal_cone_volume(), 12.4344)
        res13 = maths_class.ConeOperations(3, 4)
        self.assertNotEqual(res13.cal_cone_volume(), 15)

    def test_cal_cube_vol(self):
        res14 = maths_class.ConeOperations(2, 3)
        self.assertEqual(res14.cal_cube_volume(), 9)
        res15 = maths_class.ConeOperations(2, 3)
        self.assertNotEqual(res15.cal_cube_volume(), 9)











if __name__ == '__main__':

    unittest.main()