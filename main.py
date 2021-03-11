import MyModule
import time

a = []
buble = MyModule.MyDanSort(a)
start = time.time()
buble.get_quick_sort()
end = time.time()
print(end - start)
print(a)
del buble
