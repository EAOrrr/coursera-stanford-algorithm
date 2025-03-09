import random

def readfile(filename):
    f = open(filename)
    return [int(i) for i in f.readlines()]

def always_first(arr, start, end):
    return start

def always_final(arr, start, end):
    return end

def median_of_three(arr, start, end):
    mid = (end - start) // 2 + start
    three_min = min(arr[mid], arr[start], arr[end]) 
    three_max = max(arr[mid], arr[start], arr[end]) 

    if arr[mid] != three_min and arr[mid] != three_max:
        return mid
    if arr[start] != three_min and arr[start] != three_max:
        return start
    return end
    
def random_choice(arr, start, end):
    return random.randint(start, end)

def partition(arr, start, end):
    pivot = arr[start]
    i = start + 1
    for j in range(start + 1, end + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[start], arr[i - 1] = arr[i - 1], arr[start]
    return i - 1

def quick_sort(arr, pivot_choice):
    return quick_sort_helper(arr, 0, len(arr) - 1, pivot_choice)

def quick_sort_helper(arr, start, end, pivot_choice):
    if start >= end:
        return max(0, end - start)
    p = pivot_choice(arr, start, end)
    arr[p], arr[start] = arr[start], arr[p]
    split = partition(arr, start, end)
    left = quick_sort_helper(arr, start, split - 1, pivot_choice)
    right = quick_sort_helper(arr, split + 1, end, pivot_choice)
    return end - start + left + right

# a = [6, 3, 4, 5, 2, 1]
# quick_sort(a, always_first)
# print(a)
# a = [6, 3, 4, 5, 2, 1]
# quick_sort(a, always_final)
# print(a)
# a = [6, 3, 4, 5, 2, 1]
# quick_sort(a, median_of_three)
# print(a)
# a = [6, 3, 4, 5, 2, 1]
# quick_sort(a, random_choice)
# print(a)

arr = readfile("/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part01/Week03/QuickSort.txt")
print(quick_sort(arr[:], always_first))
print(quick_sort(arr[:], always_final))
print(quick_sort(arr[:], median_of_three))
print(quick_sort(arr[:], random_choice))