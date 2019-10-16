# TO-DO: complete the help function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []
    # TO-DO
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] < arrB[0]:
            merged_arr.append(arrA.pop(0))
        else:
            merged_arr.append(arrB.pop(0))
    if len(arrA) > 0:
        merged_arr.extend(arrA)
    if len(arrB) > 0:
        merged_arr.extend(arrB)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    # check if arr is not empty
    if len(arr) <= 1:
        return arr

    # find middle point of arr to split
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    arrA = merge_sort(left)
    arrB = merge_sort(right)

    return merge(arrA, arrB)


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
result = merge_sort(arr1)

print(result)


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
