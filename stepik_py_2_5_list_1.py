'''
Напишите программу, на вход которой подаётся список чисел одной строкой.
Программа должна для каждого элемента этого списка вывести сумму двух его соседей.
Для элементов списка, являющихся крайними, одним из соседей считается элемент,
находящий на противоположном конце этого списка.
Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).

Если на вход пришло только одно число, надо вывести его же.

Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
'''
values = [int(x) for x in input().split()]

i = 0
j = 0
new_list = []
x = 0
length_values = len(values)
for i in range(length_values):
    if len(values) <= 1:
        new_list.append(int(values[0]))
        break
    elif i == 0:
        x = int(values[-1]) + int(values[1])
        new_list.append(x)
    elif i != 0 and i < (length_values - 1):
        x = int(values[i-1]) + int(values[i+1])
        new_list.append(x)
    else:
        x = int(values[-2]) + int(values[0])
        new_list.append(x)

print(' '.join(str(x) for x in new_list))