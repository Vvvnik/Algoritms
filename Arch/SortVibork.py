import random

a = []
for x in range(1, 1000):
    a.append(random.randint(1, 1000))

print(a)


def selection_sort(arr):

    for i in range(len(arr)):
        lowest = i
        for j in range (i+1,len(arr)):
            if arr[j] < arr[lowest]:
                lowest = j # нашли меньший
        arr[i], arr[lowest] = arr[lowest], arr[i]
    return(arr)


import time

start = time.time()

b = selection_sort(a)

end = time.time()
print(end - start)

print(b)