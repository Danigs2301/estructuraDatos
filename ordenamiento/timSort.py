MIN_RUN = 32

def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1

        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key_item

def merge(arr, left, mid, right):
    len1 = mid - left + 1
    len2 = right - mid
    left_arr = [0] * len1
    right_arr = [0] * len2

    for i in range(len1):
        left_arr[i] = arr[left + i]
    for i in range(len2):
        right_arr[i] = arr[mid + 1 + i]

    i = 0
    j = 0
    k = left

    while i < len1 and j < len2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len2:
        arr[k] = right_arr[j]
        j += 1
        k += 1

def tim_sort(arr):
    n = len(arr)

    for start in range(0, n, MIN_RUN):
        end = min(start + MIN_RUN - 1, n - 1)
        insertion_sort(arr, start, end)

    size = MIN_RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)
            merge(arr, left, mid, right)
        size *= 2