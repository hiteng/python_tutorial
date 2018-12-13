
from utils import cal_perc


def income_tax(taxable_amount):

    if taxable_amount <= 50000:

        perc_amount = cal_perc(taxable_amount,.15)
    else:
        perc_amount = cal_perc(taxable_amount, .30)

    result = taxable_amount-perc_amount
    print "Salary after tax = ", result
    return result

income_tax(100000)
