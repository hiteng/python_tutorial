
def mergeSort(arr):
    if len(arr) >1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        mergeSort(left_arr)
        mergeSort(right_arr)
        i = j = k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


def printList(arr):
    out_list = []
    for i in range(len(arr)):
        out_list.append(arr[i])
    print out_list


# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7, 6, 11, 13, 5]
    printList(arr)
    mergeSort(arr)
    printList(arr)


