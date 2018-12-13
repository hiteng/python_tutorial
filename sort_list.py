

def sort_list(list_num):


    for i in range(len(list_num)):
        for j in range(i+1, len(list_num)):
            if list_num[i] > list_num[j]:
                list_num[i], list_num[j] = list_num[j], list_num[i]
    print list_num

if __name__ == '__main__':

    list_num = [1, 3, 67, 2, 43, 57, 8, 20]

    sort_list(list_num)