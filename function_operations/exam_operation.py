



from utils import perc_cal


def exam_result(total_marks, out_of_marks):

    if total_marks > out_of_marks:
        result = "Invalid marks"
        return result
    total_perc = perc_cal(total_marks,out_of_marks)
    print "total perc", total_perc

    if total_perc >= 75:
        result = "Student is passed with Distinction"
    elif total_perc >= 50:
        result = "Student is passed with First class"
    elif total_perc >= 40:
        result = "Student is passed"
    else:
        result = "Student is failed"
    return result

print "exam operation __name__ ", __name__
#print exam_result(430,500)

def exam_result1(sub1, sub2, sub3, sub4, sub5, out_of_marks):

    total_marks = sum([sub1,sub2,sub3,sub4,sub5])

    if total_marks > out_of_marks:
        result = "Invalid marks"
        return result

    total_perc = perc_cal(total_marks, out_of_marks)

    print "Total Percentage =", total_perc
    if total_perc >= 75:
        result = "Student is passed with Distinction"
    elif total_perc >= 50:
        result = "Student is passed with First class"
    elif total_perc >= 40:
        result = "Student is passed"
    else:
        result = "Student is failed"
    return result

print exam_result1(76,88,83,79,77,500)


