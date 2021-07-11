"""
Вычисление последней цифры числа Фибоначчи.
Поскольку нас интересует только последняя цифра числа Фибоначчи: если 0≤a,b≤9 — последние цифры чисел
F_i и F_i+1 соответственно, то (a+b) % 10 — последняя цифра числа F_i+2
"""


def fib_digit(n):
    fib_list = [1, 1]
    if n == 0:
        return fib_list[0]
    elif n == 1:
        return fib_list[1]
    else:
        i = 2
        while i < n:
            tmp_var = fib_list[i - 1] + fib_list[i - 2]
            fib_list.append(tmp_var % 10)
            i += 1
        return fib_list[-1]


print(fib_digit(841645))
