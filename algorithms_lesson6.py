# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Для анализа возьмите любые 1-3 ваших программы. Результаты анализа вставьте в виде комментариев к коду.
# P.S. Напишите в комментариях версию Python и разрядность ОС.

import sys
import ctypes
import struct

a = int(input('Введите трехзначное число, например (123): '))
a1 = a // 100
a2 = a % 100 // 10
a3 = a % 10
sum_a = a1 + a2 + a3
print(sum_a)
multiple_a = a1 * a2 * a3
print(multiple_a)
print('*' * 50)
print(sys.getrefcount(sum_a))
print(sys.getsizeof(sum_a))

# p.s. python 3.6,  64 разряда os
# счетчик ссылок на объет составляет 8.
# размер объекта в байтах составляет 14 байт.


a = [0]*8
for i in range(2,100):
    for j in range(2,10):
        if i%j == 0:
            a[j-2] += 1
i = 0
while i < len(a):
    print(i+2, ' - ', a[i])
    i += 1
print('*' * 50)
print(sys.getrefcount(a))
print(sys.getsizeof(a))
print('*' * 50)
print(sys.getrefcount(i))
print(sys.getsizeof(i))


# ps. количество ссылок на объект в переменной a составляет 2, в переменной  i составляет 37
# размер объекта a в байтах составляет 68 байт, объекта  i составляет 14 байт


import time
import timeit
import cProfile


start = time.time()
a = [0]*1000000
def nature_s(a):
    for i in range(2,1000000):
        for j in range(2,1000000):
            if i%j == 0:
                a[j-2] += 1
    i = 0
    while i < len(a):
        print(i+2, ' - ', a[i])
        i += 1

delta = time.time() - start
print(delta)
print(timeit.timeit())

print('*' * 50)
print(sys.getrefcount(delta))
print(sys.getsizeof(delta))

# ps. количество ссылок на объект delta составляет 2
# размер объекта delta в байтах составляет 16 байт
