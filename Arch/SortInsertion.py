import random

a = []
for x in range(1, 1000):
    a.append(random.randint(1, 1000))

print(a)


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        current_value = arr[i]
        j = i - 1
        while j >= 0:
            if current_value < arr[j]:
                arr[j+1] = arr[j]
                arr[j] = current_value
                j = j - 1
            else:
                break
    return arr

import time

start = time.time()

b = insertion_sort(a)

end = time.time()
print(end - start)

print(b)

