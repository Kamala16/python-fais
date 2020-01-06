import listy 
import timeit
import matplotlib
import matplotlib.pyplot as plt

def swap(L, left, right):
    item = L[left]
    L[left] = L[right]
    L[right] = item

# SELECTSORT

def selectsort(L, left, right):
    
    for i in range(left, right):
        k = i
        for j in range(i+1, right+1):
            if L[j] < L[k]:
                k = j
        item = L[k]
        while k > i:
            L[k] = L[k-1]
            k = k-1
        L[i] = item
    return L

# INSERTSORT

def insertsort(L, left, right):
    for i in range(left+1, right+1):
        item = L[i]
        j = i
        while j > left and L[j-1] > item:
            L[j] = L[j-1]
            j = j-1
        L[j] = item

# BUBBLESORT

def bubblesort(L, left, right):
    for i in range(left, right):
        for j in range(left, right):
            if L[j] > L[j+1]:
                swap(L, j+1, j)

# QUICKSORT

def quicksort(L, left, right):
    if left >= right:
        return
    pivot = partition(L, left, right)
    quicksort(L, left, pivot - 1)
    quicksort(L, pivot + 1, right)

def partition(L, left, right):
    x = L[right]
    i = left
    for j in range(left, right):
        if L[j] <= x:
            swap(L, i, j)
            i += 1
    swap(L, i, right)
    return i

# COUNTINGSORT
def countingsort(array):
    size = len(array)
    output = [0] * size
    count = [0] * size
    for i in range(0, size):
        count[array[i]] += 1
    for i in range(1, size):
        count[i] += count[i - 1]
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1
    for i in range(0, size):
        array[i] = output[i]


print("SELECTSORT:")
czas_select_10_2 = (timeit.timeit(lambda: selectsort(listy.int_0_N1(100), 0, len(listy.int_0_N1(100))-1), number= 1))
czas_select_10_3 = (timeit.timeit(lambda: selectsort(listy.int_0_N1(1000), 0, len(listy.int_0_N1(1000))-1), number= 1))
czas_select_10_4 = (timeit.timeit(lambda: selectsort(listy.int_0_N1(10000), 0, len(listy.int_0_N1(10000))-1), number= 1))
print('10**2: {:.5}'.format(czas_select_10_2))
print('10**3: {:.5}'.format(czas_select_10_3))
print('10**4: {:.5}'.format(czas_select_10_4))

print("INSERTSORT:")
czas_insert_10_2 = (timeit.timeit(lambda: insertsort(listy.int_0_N1(100), 0, len(listy.int_0_N1(100))-1), number= 1))
czas_insert_10_3 = (timeit.timeit(lambda: insertsort(listy.int_0_N1(1000), 0, len(listy.int_0_N1(1000))-1), number= 1))
czas_insert_10_4 = (timeit.timeit(lambda: insertsort(listy.int_0_N1(10000), 0, len(listy.int_0_N1(10000))-1), number= 1))
print('10**2: {:.5}'.format(czas_insert_10_2))
print('10**3: {:.5}'.format(czas_insert_10_3))
print('10**4: {:.5}'.format(czas_insert_10_4))

print("BUBBLESORT:")
czas_bubble_10_2 = (timeit.timeit(lambda: bubblesort(listy.int_0_N1(100), 0, len(listy.int_0_N1(100))-1), number= 1))
czas_bubble_10_3 = (timeit.timeit(lambda: bubblesort(listy.int_0_N1(1000), 0, len(listy.int_0_N1(1000))-1), number= 1))
czas_bubble_10_4 = (timeit.timeit(lambda: bubblesort(listy.int_0_N1(10000), 0, len(listy.int_0_N1(10000))-1), number= 1))
print('10**2: {:.5}'.format(czas_bubble_10_2))
print('10**3: {:.5}'.format(czas_bubble_10_3))
print('10**4: {:.5}'.format(czas_bubble_10_4))

print("QUICKSORT:")
czas_quick_10_2 = (timeit.timeit(lambda: quicksort(listy.int_0_N1(100), 0, len(listy.int_0_N1(100))-1), number= 1))
czas_quick_10_3 = (timeit.timeit(lambda: quicksort(listy.int_0_N1(1000), 0, len(listy.int_0_N1(1000))-1), number= 1))
czas_quick_10_4 = (timeit.timeit(lambda: quicksort(listy.int_0_N1(10000), 0, len(listy.int_0_N1(10000))-1), number= 1))
czas_quick_10_5 = (timeit.timeit(lambda: quicksort(listy.int_0_N1(100000), 0, len(listy.int_0_N1(100000))-1), number= 1))
czas_quick_10_6 = (timeit.timeit(lambda: quicksort(listy.int_0_N1(1000000), 0, len(listy.int_0_N1(1000000))-1), number= 1))
print('10**2: {:.5}'.format(czas_quick_10_2))
print('10**3: {:.5}'.format(czas_quick_10_3))
print('10**4: {:.5}'.format(czas_quick_10_4))
print('10**5: {:.5}'.format(czas_quick_10_5))
print('10**6: {:.5}'.format(czas_quick_10_6))

print("COUNTINGSORT:")
czas_count_10_2 = (timeit.timeit(lambda: countingsort(listy.int_0_N1(100)), number= 1))
czas_count_10_3 = (timeit.timeit(lambda: countingsort(listy.int_0_N1(1000)), number= 1))
czas_count_10_4 = (timeit.timeit(lambda: countingsort(listy.int_0_N1(10000)), number= 1))
czas_count_10_5 = (timeit.timeit(lambda: countingsort(listy.int_0_N1(100000)), number= 1))
czas_count_10_6 = (timeit.timeit(lambda: countingsort(listy.int_0_N1(1000000)), number= 1))
print('10**2: {:.5}'.format(czas_count_10_2))
print('10**3: {:.5}'.format(czas_count_10_3))
print('10**4: {:.5}'.format(czas_count_10_4))
print('10**5: {:.5}'.format(czas_count_10_5))
print('10**6: {:.5}'.format(czas_count_10_6))
