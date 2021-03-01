import random

a = []
for j in range(1, 1000):
    a.append(random.randint(1, 1000))

print(a)

def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        less = [x for x in arr if x < pivot]
        greater_or_equal = [x for x in arr if x >= pivot]
        return quick_sort(less) + quick_sort(greater_or_equal)

sort = quick_sort(a)

print(a)

