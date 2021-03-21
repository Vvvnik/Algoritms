# -*- coding: utf-8 -*-
import MyModule
import time


# Функция декоратор расчета времени выполнения различных алгоритмов
def decorator_calc_time(algoritmSort):
    start = time.time()
    print(algoritmSort)
    end = time.time()
    return end-start


buble = MyModule.MyDanSort([])
print(decorator_calc_time(buble.get_quick_sort()))
del buble
