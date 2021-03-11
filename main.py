import random
import MyModule
import time

#     from MyModule import MyDanSort

a = []

buble = MyModule.MyDanSort(a)

print(buble.get_quick_sort())
print('Yes')
del buble

a = []
for x in range(1, 300):
    a.append(random.randint(601, 1000))

for x in range(1, 300):
    a.append(random.randint(301, 600))

for x in range(1, 400):
    a.append(random.randint(1, 300))
print(a)

start = time.time()

MyModule.bubble_sort2(a)
end = time.time()
print(end - start)

print(a)
