# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.


a = [0]*8
for i in range(2,100):
    for j in range(2,10):
        if i%j == 0:
            a[j-2] += 1
i = 0
while i < len(a):
    print(i+2, ' - ', a[i])
    i += 1
    
    # 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 0, 3, 4, 5
# (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

from random import random
N = 10
arr = [0]*N
even = []
for i in range(N):
    arr[i] = int(random() * 10) + 10
    if arr[i] % 2 == 0:
        even.append(i)
print(arr)
print('Индексы четных элементов: ', even)


# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import random
N = 15
arr = [0]*N
for i in range(N):
    arr[i] = int(random()*100)
    print(arr[i],end=' ')
print()
mn = 0
mx = 0
for i in range(N):
    if arr[i] < arr[mn]:
        mn = i
    elif arr[i] > arr[mx]:
        mx = i
print('arr[{}]={} arr[{}]={}'.format(mn+1, arr[mn], mx+1, arr[mx]))
b = arr[mn]
arr[mn] = arr[mx]
arr[mx] = b

for i in range(15):
    print(arr[i], end=' ')
print()

# 4. Определить, какое число в массиве встречается чаще всего.

from random import random

N = 27
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 20)
print(arr)

num = arr[0]
max_frq = 1
for i in range(N - 1):
    frq = 1
    for k in range(i + 1, N):
        if arr[i] == arr[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = arr[i]

if max_frq > 1:
    print(max_frq, 'раз(а) встречается число', num)
else:
    print('Все элементы уникальны')
    
    # 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import random

N = 15
arr = []
for i in range(N):
    arr.append(int(random() * 100) - 15)
print(arr)

i = 0
index = -1
while i < N:
    if arr[i] < 0 and index == -1:
        index = i
    elif arr[i] < 0 and arr[i] > arr[index]:
        index = i
    i += 1

print(index + 1, ':', arr[index])

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
from random import random

N = 10
a = [0]*N
for i in range(N):
    a[i] = int(random()*50)
    print('{}'.format(a[i], end=''))
print()

min_id = 0
max_id = 0
for i in range(1,N):
    if a[i] < a[min_id]:
        min_id = i
    elif a[i] > a[max_id]:
        max_id = i
print(a[min_id], a[max_id])

if min_id > max_id:
    min_id, max_id = max_id, min_id

summa = 0
for i in range(min_id+1, max_id):
    summa += a[i]
print(summa)

# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from random import random

N = 10
a = []
for i in range(N):
    a.append(int(random() * 100))
    print("{}".format(a[i], end=''))
print()

if a[0] > a[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0

for i in range(2, N):
    if a[i] < a[min1]:
        b = min1
        min1 = i
        if a[b] < a[min2]:
            min2 = b
    elif a[i] < a[min2]:
        min2 = i

print("№{}:{}".format(min1 + 1, a[min1]))
print("№{}:{}".format(min2 + 1, a[min2]))

# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# # Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку.
# # В конце следует вывести полученную матрицу.

M = 5
N = 4
a = []
for i in range(N):
    b = []
    s = 0
    print("{}-я строка:".format(i))
    for j in range(M - 1):
        n = int(input())
        s += n
        b.append(n)
    b.append(s)
    a.append(b)

for i in a:
    print(i)
    
    # 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import random

M = 10
N = 5
a = []
for i in range(N):
    b = []
    for j in range(M):
        n = int(random() * 200)
        b.append(n)
        print('{}'.format(n, end=''))
    a.append(b)
    print()

mx = -1
for j in range(M):
    mn = 200
    for i in range(N):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
print("Максимальный среди минимальных: ", mx)
