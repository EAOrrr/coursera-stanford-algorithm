def build_array(filename):
    f = open(filename)
    return [int(i) for i in f.readlines()]

def count_cross_inversions(array, start, mid, end):
    i = 0
    j = 0
    k = start
    left = array[start: mid]
    right = array[mid: end]
    cnt = 0
    while i < mid - start and j < end - mid:
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
            cnt += j
        else:
            array[k] = right[j]
            j += 1
        k += 1
    while i < mid - start:
        array[k] = left[i]
        k += 1
        i += 1
        cnt += j
    while j < end - mid:
        array[k] = right[j]
        k += 1
        j += 1
    return cnt

def count_inversions(array, start, end):
    if start + 1 >= end:
        return 0
    mid = (end - start)//2 + start
    left_inv = count_inversions(array, start, mid)
    right_inv = count_inversions(array, mid, end)
    cross_inv = count_cross_inversions(array, start, mid, end)
    return left_inv + right_inv + cross_inv

a = build_array("/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part01/Week02/IntegerArray.txt")
# a = [6, 3, 4, 5, 2, 1]
print(count_inversions(a, 0, len(a)))
# print(a)