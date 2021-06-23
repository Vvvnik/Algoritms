# -*- coding: utf-8 -*-
# проект проверяет скорость работы различных алгоритмов сортировки
# в main.py считается скорость и вызываются алгоритмы в методах класса в модуле MyModule.py
# методы вызываются в зависимости от условия Decorator или через декоратор где считается время
# или без декоратора
import MyModule
import time


# Функция декоратор + расчет времени выполнения различных алгоритмов
def decorator_calc_time(algoritmsSort):
    starter = time.time()
    print("Отсортированный список :  ")
    print(algoritmsSort)
    print("Время выполнения :  ")
    endear = time.time()
    return endear-starter


buble = MyModule.MyDanSort([]) # создется экземпляр класса MyDanSort
# Decorator =1 или = 0 или функция из класса вызывается через декоратор или напрямую (напрямую дольше, почему?)
#   get_quick_sort в полтора раза отличается
#   getInsertionSort в 57!
#   причем c декоратором все функции работают быстро
Decorator = 0
if Decorator:
    x = print(decorator_calc_time(buble.getInsertionSort()))
else:
    starter = time.time()
    print("Отсортированный список :  ")
    print(buble.MyQuickSort())
    endear = time.time()
    print("Время выполнения :  ")
    print(endear-starter)

del buble
