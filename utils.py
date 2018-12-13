from __future__ import division


def cal_perc(inp1,pr_value):
    result = inp1 * pr_value
    return result

def perc_cal(inp_no,out_of):

    perc = (inp_no/out_of)*100
    return perc

print "utils __name__ ", __name__
if __name__ == "__main__":

    print perc_cal(200,500)


def perc_cal1(inp_no1, inp_no2, inp_no3, inp_no4, inp_no5, out_of):

    perc1 = (((inp_no1+inp_no2+inp_no3+inp_no4+inp_no5)/out_of)*100)
    return perc1


if __name__== "__main__":


    print perc_cal1(80,75,85,75,90,500)


