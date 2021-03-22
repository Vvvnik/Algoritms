import random

a = []
for x in range(1, 1000):
    a.append(random.randint(1, 1000))

print(a)

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

import time

start = time.time()

b = selection_sort(a)

end = time.time()
print(end - start)

print(b)