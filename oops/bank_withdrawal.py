


class BankTransaction(object):

    bal = 100000


    def __init__(self, with_amt=None, dep_amt=None):

        self.with_amt = with_amt
        self.dep_amt = dep_amt

    def bank_withdraw(self):
        return self.bal - self.with_amt

    def bank_deposit(self):
        return self.bal + self.dep_amt

class MinimumBalance(BankTransaction):

    def __init__(self, with_amt):

        self.with_amt = with_amt
        super(MinimumBalance, self).__init__(with_amt=with_amt)

    def late_fee(self):
        fee_pen = self.bank_withdraw()
        if fee_pen < 50000:
            print "Balance after penalty fee : ", fee_pen - 1000

class InterestOnBalance(BankTransaction):

    def __init__(self, dep_amt):
        self.dep_amt = dep_amt
        super(InterestOnBalance, self).__init__(dep_amt=dep_amt)

    def interest_added(self):
        int_amt = self.bank_deposit()
        if int_amt >= 100000:
            print "Balance after adding interest : ", int_amt + (.15 * self.bal)
        elif int_amt > 50000 and int_amt < 100000:
            print "Balance after adding interest : ", int_amt + (.10 * self.bal)
        else:
            print "Balance after adding interest : ", int_amt + (.05 * self.bal)


if __name__ == '__main__':


    bal_amount = input("Enter the amount : ")


    # obj = BankTransaction(bal_amount)
    # print obj.bank_withdraw()
    #
    # obj_1 = BankTransaction(0, bal_amount)
    # print obj_1.bank_deposit()

    obj_2 = MinimumBalance(bal_amount)
    obj_2.late_fee()

    obj_3 = InterestOnBalance(bal_amount)
    obj_3.interest_added()