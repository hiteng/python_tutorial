


class SalaryMod(object):



    def __init__(self, sal=None, int=None):
        self.sal = sal
        self.int = int

    def sal_interest_cal(self):
        if self.sal <= 50000:
            sal_int = self.sal * .15
            return self.sal - sal_int

        elif self.sal > 50000 and self.sal <= 100000:
            sal_int1 = self.sal * .20
            return self.sal - sal_int1

        elif self.sal >100000 and self.sal <= 200000:
            sal_int2 = self.sal * .25
            return self.sal - sal_int2


class SalaryBonus(SalaryMod):

    def __init__(self, sal):
        self.sal = sal

    def sal_interest_cal(self):

        result = super(SalaryBonus, self).sal_interest_cal()
        if self.sal <= 50000:
            return result + (.05 * 50000)
        elif self.sal > 50000 and self.sal <= 100000:
            return result + (.10 * 100000)
        else:
            return result + (.15 * 200000)


if __name__ == '__main__':

    salary_var = input("Enter the salary amount: ")

    obj = SalaryMod(salary_var)
    print obj.sal_interest_cal()

    obj_1 = SalaryBonus(salary_var)
    print obj_1.sal_interest_cal()
