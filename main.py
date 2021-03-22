# -*- coding: utf-8 -*-
import MyModule
import time


# Функция декоратор расчета времени выполнения различных алгоритмов
def decorator_calc_time(algoritmsSort):
    starter: float = time.time()
    print(algoritmsSort)
    endear = time.time()
    return endear-starter


buble = MyModule.MyDanSort([])
Decorator = 0
if Decorator:
    x = print(decorator_calc_time(buble.getInsertionSort()))
else:
    starter = time.time()
    print(buble.getInsertionSort())
    endear = time.time()
    print(endear-starter)
del buble
