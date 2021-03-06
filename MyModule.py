# -*- coding: utf-8 -*-
import random


class MyDanSort:


    def __init__(self, a):
        self.a = a
        n = 1000
        for x in range(n):
            self.a.append(random.randint(0, n))

    def MyQuickSort(self):
        def _quick_sort(s):
            if len(s) <= 1:
                return s
            ref = s[0]
            left = list(filter(lambda x: x < ref, s))
            center = [i for i in s if i == ref]
            right = list(filter(lambda x: x > ref, s))
            return _quick_sort(left) + center + _quick_sort(right)

        return(_quick_sort(self.a))

    def get_bubble_sort(self):
        n = len(self.a)
        for i in range(n):
            for j in range(n - i - 1):
                if self.a[j] > self.a[j + 1]:
                    self.a[j], self.a[j + 1] = self.a[j + 1], self.a[j]
        return self.a

    def partition(self, low, high):
        # Мы выбираем средний элемент, в качестве опорного. Некоторые реализации выбирают
        # первый элемент или последний элемент или вообще случайный элемент.
        r = (len(self.a)) // 2
        p = self.a[r]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while self.a[i] < p:
                i += 1
            j -= 1
            while self.a[j] > p:
                j -= 1
            if i >= j:
                return j
            # Если элемент в i (слева от оси) больше, чем
            # элемент в J (справа от оси), то поменять их местами
            self.a[i], self.a[j] = self.a[j], self.a[i]

    def get_quick_sort(self):  # самая быстрая функция сортировки в 2 раза быстрее MyQuickSort
        # Создаем вспомогательную рекурсивную функцию def partition(self, low, high): выше

        def _quick_sort(items, low, high):

            if low < high:
                # Это индекс после опорного элемента, по которому наши списки разделены
                split_index = partition(items, low, high)
                _quick_sort(items, low, split_index)
                _quick_sort(items, split_index + 1, high)
        _quick_sort(self.a, 0, len(self.a) - 1)
        return self.a

    def getInsertionSort(self):
        n = len(self.a)
        for i in range(n):
            current_value = self.a[i]
            j = i - 1
            while j >= 0:
                if current_value < self.a[j]:
                    self.a[j + 1] = self.a[j]
                    self.a[j] = current_value
                    j = j - 1
                else:
                    break
        return self.a

    def getSelectionSort(self):
        n = len(self.a)
        for i in range(n):
            lowest = i
            for j in range(i + 1, n):
                if self.a[j] < self.a[lowest]:
                    lowest = j  # нашли меньший
            self.a[i], self.a[lowest] = self.a[lowest], self.a[i]
        return self.a


def MyReadTxtFile(name_file):
    f = open(name_file, 'r')
    a = f.read()
    f.close()
    return a


def revers_string(s):
    chars = list(s)

    for i in range(len(s)//2):
        temp = chars[i]
        chars[i] = chars[len(s)-i-1]
        chars[len(s)-i-1] = temp
    return ''.join(chars)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def bubble_sort2(s):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for index in range(len(s)-1):
            current = s[index]
            my_next = s[index + 1]
            if current > my_next:
                is_sorted = False
                s[index] = my_next
                s[index + 1] = current
    return s


def heapify(nums, heap_size, root_index):
    # Предположим, что индекс самого большого элемента является корневым индексом
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2
    # Если левый потомок корня является допустимым индексом, а элемент больше
    # чем текущий самый большой элемент, то обновляем самый большой элемент
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child
    # Делайте то же самое для right_child
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child
    # Если самый большой элемент больше не является корневым элементом, меняем их местами
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(nums, heap_size, largest)


def heap_sort(nums):
    n = len(nums)
    # Создаем Max Heap из списка
    # Второй аргумент означает, что мы останавливаемся на элементе перед -1, то есть на первом элементе списка.
    # Третий аргумент означает, что мы повторяем в обратном направлении, уменьшая количество i на 1
    for i in range(n, -1, -1):
        heapify(nums, n, i)
    # Перемещаем корень max hea в конец
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


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


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result


def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        middle = int(len(arr) / 2)
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge(left, right)


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


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q]

    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)


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


def selection_sort2(arr):

    for i in range(len(arr)):
        lowest = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[lowest]:
                lowest = j
        arr[i], arr[lowest] = arr[lowest], arr[i]
    return arr
