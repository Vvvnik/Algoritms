import random

a = []
for x in range(1, 1000):
    a.append(random.randint(1, 1000))

print(a)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

import time

start = time.time()

b = bubble_sort(a)

end = time.time()
print(end - start)

print(b)