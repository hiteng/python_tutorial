


class SalaryMod(object):



    def __init__(self, sal=None, int=None):
        self.sal = sal
        self.int = int

    def sal50(self):
        if self.sal < 50000:
            sal_int = self.sal * .15
            return self.sal - sal_int

        elif self.sal > 50000 and self.sal < 100000:
            sal_int1 = self.sal * .20
            return self.sal - sal_int1

        elif self.sal >100000 and self.sal < 200000:
            sal_int2 = self.sal * .25
            return self.sal - sal_int2

    def salgen(self):
        sal_gen = self.sal50 * 3
        return sal_gen

    def sal100(self):
        sal_int1 = self.sal * .20
        return self.sal - sal_int1

    def sal150(self):
        sal_int2 = self.sal * .25
        return self.sal - sal_int2

if __name__ == '__main__':


    obj = SalaryMod(input("Enter the salary amount: "))
    print obj.sal50()
    print obj.salgen()