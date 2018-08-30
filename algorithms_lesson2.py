# Каждую задачу сохраните в отдельный файл.
# В начале файла вставьте текст ДЗ.
# Блок-схемы создайте на сайте draw.io и приложите ссылку в комментарии к ДЗ.
#
# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
# сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль,
# если он ввел 0 в качестве делителя.

print("Ноль завершит работу программы")
while True:
        s = input("Знак (+,-,*,/): ")
        if s == '0': break
        if s in ('+','-','*','/'):
                x = float(input("x="))
                y = float(input("y="))
                if s == '+':
                        print("{}".format(x+y))
                elif s == '-':
                        print("{}".format(x-y))
                elif s == '*':
                        print("{}".format(x*y))
                elif s == '/':
                        if y != 0:
                                print("{}".format(x/y))
                        else:
                                print("Деление на ноль!")
        else:
                print("Неверный знак операции!")

# https://drive.google.com/file/d/1xYG2zipssUW28geht0h-GhEGi4UgdF-x/view?usp=sharing


# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

n = int(input())
even=odd=0
while n>0:
    if n%2 == 0:
        even += 1
    else:
        odd += 1
    n = n//10
print("четных - {}, нечетных - {}".format(even, odd))


# https://drive.google.com/file/d/1xYG2zipssUW28geht0h-GhEGi4UgdF-x/view?usp=sharing

# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

n = int(input())
m = 0
while n>0:
    m = m*10 + n%10
    n = n//10
print(m)

# https://drive.google.com/file/d/1xYG2zipssUW28geht0h-GhEGi4UgdF-x/view?usp=sharing

#4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

n = int(input())
e = 1
s = 0
for i in range(n):
    s += e
    e /= -2
print(s)


# https://drive.google.com/file/d/1xYG2zipssUW28geht0h-GhEGi4UgdF-x/view?usp=sharing


# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# # Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.


for i in range(32, 128):
    print("{}-{}".format(i, chr(i)), end='')
    if i % 10 == 0:
        print()

print()

# https://drive.google.com/file/d/1xYG2zipssUW28geht0h-GhEGi4UgdF-x/view?usp=sharing

# 6. В программе генерируется случайное целое число от 0 до 100. Пользовате
# ль должен его отгадать не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться,
# больше или меньше загаданного введенное пользователем число. Если за 10 попыток число не отгадано, то вывести его.

from random import random
n = round(random() * 100)
i = 1
print("Компьютер загадал число. Отгадайте его. У вас 10 попыток")
while i <= 10:
    u = int(input(str(i) + '-я попытка: '))
    if u > n:
        print('Много')
    elif u < n:
        print('Мало')
    else:
        print('Вы угадали с {}-й попытки'.format(i)
        break
    i += 1
else:
    print('Вы исчерпали 10 попыток. Было загадано', n)

# https://drive.google.com/file/d/1xYG2zipssUW28geht0h-GhEGi4UgdF-x/view?usp=sharing

# 7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется
# равенство: 1+2+...+n = n(n+1)/2, где n – любое натуральное число.

n = int(input())
s = 0
for i in range(1,n+1):
    s += i
m = n * (n + 1) // 2
print(s)
print(m)


# https://drive.google.com/file/d/1xYG2zipssUW28geht0h-GhEGi4UgdF-x/view?usp=sharing

# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

n = int(input("Сколько будет чисел? "))
d = int(input("Какую цифру считать? "))
count = 0
for i in range(1, n + 1):
    m = int(input("Число " + str(i) + ": "))
    while m > 0:
        if m % 10 == d:
            count += 1
        m = m // 10

print("Было введено {} цифр {}".format(count, d))


# https://drive.google.com/file/d/1xYG2zipssUW28geht0h-GhEGi4UgdF-x/view?usp=sharing


# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.



n = int(input())
max_s = 0
max_m = 0
while n != 0:
    m = n
    s = 0
    while n>0:
        s += n%10
        n //= 10
    if s > max_s:
        max_s = s
        max_m = m

print('Число',max_m,'имеет максимальную сумму цифр:', max_s)

# https://drive.google.com/file/d/1xYG2zipssUW28geht0h-GhEGi4UgdF-x/view?usp=sharing
