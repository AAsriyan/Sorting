# TO-DO: complete the helpe function below to merge 2 sorted arrays


def merge(arr, leftArr, rightArr):
    i, j, k = 0, 0, 0

    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] < rightArr[j]:
            arr[k] = leftArr[i]
            i += 1
        else:
            arr[k] = rightArr[j]
            j += 1
        k += 1

    while i < len(leftArr):
        arr[k] = leftArr[i]
        i += 1
        k += 1

    while j < len(rightArr):
        arr[k] = rightArr[j]
        j += 1
        k += 1

# # TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    print("Splitting ", arr)
    if len(arr) > 1:
        mid = len(arr)//2
        leftArr = arr[:mid]
        rightArr = arr[mid:]

        merge_sort(leftArr)
        merge_sort(rightArr)

        merge(arr, leftArr, rightArr)
    print("Merging ", arr)
    return arr


testArr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(testArr)

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
