# -*- coding: utf-8 -*-
import MyModule
import time


# Функция декоратор расчета времени выполнения различных алгоритмов
def decorator_calc_time(algoritmsSort):
    start = time.time()
    print(algoritmsSort)
    end = time.time()
    return end-start


buble = MyModule.MyDanSort([])
print(round(decorator_calc_time(buble.getInsertionSort()), 4))
del buble
