
a=[4,6,2,3,5,7,9,0,8,1]

print(a)

import random

def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        less = [x for x in arr if x < pivot]
        greater_or_equal = [x for x in arr if x >= pivot]
        return quick_sort(less) + quick_sort(greater_or_equal)

print(quick_sort(a))
