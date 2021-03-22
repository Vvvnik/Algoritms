# -*- coding: utf-8 -*-
import MyModule
import time


# Функция декоратор расчета времени выполнения различных алгоритмов
def decorator_calc_time(algoritmsSort):
    starter = time.time()
    print(algoritmsSort)
    endear = time.time()
    return endear-starter


buble = MyModule.MyDanSort([])
# Decorator =1 или = 0 или функция из класса вызывается через декоратор или напрямую (напрямую дольше, почему?)
#   get_quick_sort в полтора раза отличается
#   getInsertionSort в 57!
#   причем c декоратором все функции работают быстро
Decorator = 1
if Decorator:
    x = print(decorator_calc_time(buble.getInsertionSort()))
else:
    starter = time.time()
    print(buble.getInsertionSort())
    endear = time.time()
    print(endear-starter)
del buble
