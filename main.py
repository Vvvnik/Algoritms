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
Decorator = 1
start = time.time()
if Decorator:
    x= decorator_calc_time(buble.getInsertionSort())
else:
    print(buble.getInsertionSort())
end = time.time()
print(end-start)
del buble


