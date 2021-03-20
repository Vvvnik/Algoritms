import MyModule
import time
import random


buble = MyModule.MyDanSort([])
start = time.time()
print(buble.get_quick_sort())
end = time.time()
print(end - start)
del buble


