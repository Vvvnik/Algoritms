import random

a = []
for x in range(1, 1000):
    a.append(random.randint(1, 1000))

print(a)

# схема Tony Hoare
def partition(nums, low, high):
    # Мы выбираем средний элемент, в качестве опорного. Некоторые реализации выбирают
    # первый элемент или последний элемент или вообще случайный элемент.
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        # Если элемент в i (слева от оси) больше, чем
        # элемент в J (справа от оси), то поменять их местами
        nums[i], nums[j] = nums[j], nums[i]
def quick_sort(nums):  
    # Создаем вспомогательную рекурсивную функцию
    def _quick_sort(items, low, high):
        if low < high:
            # Это индекс после опорного элемента, по которому наши списки разделены
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)
    _quick_sort(nums, 0, len(nums) - 1)
# Проверяем, что все работает

import time

start = time.time()
quick_sort(a)
end = time.time()

print(end - start)
print(a)