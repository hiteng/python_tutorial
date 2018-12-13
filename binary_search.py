
def binarySearch(arr, l, r, x):


    if r >= l:

        mid = l + (r - l) / 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1

arr = [3, 3, 7, 20, 60]
x = 20

result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print "Target Number is present at index %d" % result
else:
    print "Target Number is not present in array"
