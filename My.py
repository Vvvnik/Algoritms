import random
MyStr=[]
for i in range(1,1000):
    MyStr.append(random.randint(0,1000))
print(MyStr)

def MySort1(mas):
    k=len(mas)
    i=0
    while i<k-1:
        mas[i],mas[i+1] = mas[i+1],mas[i]
        i+=1

def MySort2(mas):
    for i in range(1,999):
        mas[i-1],mas[i] = mas[i],mas[i-1]

MySort1(MyStr)
print(MyStr)
MySort2(MyStr)
print(MyStr)


<<<<<<< HEAD
a= {'BMW','Mersedes','Audi','Porshe'}
=======
a= (['BMW',7,'white'],['Mersedes','black'],['Audi','red'],'Porshe')
>>>>>>> my
for i in enumerate(a):
    print(i)

a = [10, 20, 30, 40]
d = [123]
for i in range(len(a)):
    a[i]+=1

print(a)
