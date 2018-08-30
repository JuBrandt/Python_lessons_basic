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
