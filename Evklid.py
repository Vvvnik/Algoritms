#Алгоритм нахождения наибольшего общего делителя НОД

def gcd(a,b):
    while a !=0 and b !=0:
        if a>b:
            a= a % b
        else:
            b = b % a
    return a+b

print('Нод чисел 30, 18 = ', gcd(30,18) )

# С модуля math
import math
print('Нод чисел от Math 30, 18 = ', math.gcd(30,18))

