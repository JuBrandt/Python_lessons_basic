# 1. Проанализировать скорость и сложность одного - трёх любых алгоритмов,
# разработанных в рамках домашнего задания первых трех уроков.

import time
import timeit
import cProfile


# # 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

# start = time.time()
# a = [0]*1000000
# def nature_s(a):
#     for i in range(2,1000000):
#         for j in range(2,1000000):
#             if i%j == 0:
#                 a[j-2] += 1
#     i = 0
#     while i < len(a):
#         print(i+2, ' - ', a[i])
#         i += 1
#
# delta = time.time() - start
# print(delta)
# print(timeit.timeit())
# cProfile.run('nature(a)')

# я немного изменила алгоритм, увеличив размер списка и диапозоны, тк скорость близка к 0
# сложность алгоримта составляет O(n^2), два цикла один вложен в другой
# 0.003000020980834961
# 0.014595672670131754
# ncalls tottime  percall  cumtime  percall filename:lineno(function)
#  1       0.000    0.000    0.000    0.000 <string>:1(<module>)
#  1       0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#  1       0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# # Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку.
# # В конце следует вывести полученную матрицу.

# start = time.time()
# a = []
# def maximus_prime():
#     M = 5
#     N = 4
#     for i in range(N):
#         b = []
#         s = 0
#         print("{}-я строка:".format(i))
#         for j in range(M - 1):
#             n = int(input('Ввести число'))
#             s += n
#             b.append(n)
#         b.append(s)
#         a.append(b)
#
#     for i in a:
#         print(i)
# print(maximus_prime())
# delta = time.time() - start
# print(delta)
# print(maximus_prime())
# cProfile.run(maximus_prime())

# сложность алгоритма составляет O(n^2 + n)
# 15.489885807037354

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
#
# from random import random
#
# start = time.time()
# N = 15
# arr = [0]*N
# def five_element(N):
#     for i in range(N):
#         arr[i] = int(random()*100)
#         print(arr[i],end=' ')
#     print()
#     mn = 0
#     mx = 0
#     for i in range(N):
#         if arr[i] < arr[mn]:
#             mn = i
#         elif arr[i] > arr[mx]:
#             mx = i
#     print('arr[{}]={} arr[{}]={}'.format(mn+1, arr[mn], mx+1, arr[mx]))
#     b = arr[mn]
#     arr[mn] = arr[mx]
#     arr[mx] = b
#
#     for i in range(15):
#         print(arr[i], end=' ')
#     print()
#
# delta = time.time() - start
# print(delta)
# print(timeit.timeit(five_element(N)))
# cProfile.run(five_element(N))

# сложно алгоритма составляет O(100n + n + n) = O(n)
# 0.0





# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Первый - использовать алгоритм решето Эратосфена.
# Второй - без использования "решета". Проанализировать скорость и сложность алгоритмов.
# Примечание: Результаты анализа сохранить в виде комментариев в файле с кодом.




# решето Эратосфена
import time
import timeit
import cProfile

start = time.time()
n = int(input('Вывод простых чисел до числа: '))

def eratosfen():
    a = [0] * n
    for i in range(n):
        a[i] = i
    a[1] = 0
    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    del a
    print(b)
delta = time.time() - start
print(delta)
print(timeit.timeit(eratosfen()))
cProfile.run('eratosfen()')
# 2.1330158710479736 скорость функции
сложность алгоритма составляет O(nLog(Logn))

from math import sqrt
import cProfile

start_i = time.time()
count = 10
def kuku():
    for i in range(10):
        n = int(input())
        for j in range(2, int(sqrt(n)) + 1):
            if n % j == 0:
                count -= 1
                break

print(count)
delta_i = time.time() - start
print(delta_i)
print(timeit.timeit(count))
cProfile.run(kuku())

# 2.6521518230438232 - скорость
# 3.102177619934082 - повторно измерено
# сложность алгоритма составляет O(n^2)

#Здравствуйте, Алексей, я с удовольствием сделала бы задание в разных файлах, но дело в том что при pull request 
#на каждый файл формируется своя одтельная ссылка, а в GeekBrains на вкладке, где прикрепляют ссылку ДЗ в github, можно прикрепить
#только одну ссылку. Поэтому все задания я отправляю в одном файле.
