
import random



def list_comp_overlap():

    over_list1 = random.sample(range(100), 10)
    print over_list1
    over_list2 = random.sample(range(90), 14)
    print over_list2

    print set(over_list1).intersection(over_list2)




list_comp_overlap()