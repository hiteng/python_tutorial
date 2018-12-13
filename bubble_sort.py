
def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print ("Sorted array is:")
    out_list = []
    for i in range(len(arr)):
        out_list.append(arr[i])
    print out_list

if __name__ == '__main__':


    arr = [64, 34, 25, 12, 22, 11, 90]

    bubbleSort(arr)
