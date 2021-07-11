"""
Максимум в скользящем окне
Найти максимум в каждом окне размера m данного массива чисел A[1...n].
Вход. Массив чисел A[1...n] и число 1 ≤ m ≤ n.
Выход. Максимум подмассива A[i...i + m − 1] для всех 1 ≤ i ≤ n − m + 1.
"""
from collections import deque as dq

n = int(input())
test_list = list(map(int, input().split()))
m = int(input())
# Дека хранит индексы элементов списка
max_deque = dq()
# Записываем индексы первых m элементов. Если дека хранит индексы элементов, меньших, чем новый, удаляем их
# до тех пор, пока все элементы больше текущего
for i in range(m):
    while max_deque and test_list[i] >= test_list[max_deque[-1]]:
        max_deque.pop()
    max_deque.append(i)
# Запускаем цикл от m до конца и печатаем первый максимум == test_list[max_deque[0]]
for i in range(m, n):
    print(test_list[max_deque[0]], end=" ")
    # Удаляем элемент из начала очереди, двигая окно вправо
    while max_deque and max_deque[0] <= i - m:
        max_deque.popleft()
    # Записываем индексы первых m элементов. Если дека хранит индексы элементов, меньших, чем новый, удаляем их
    # до тех пор, пока все элементы больше текущего
    while max_deque and test_list[i] >= test_list[max_deque[-1]]:
        max_deque.pop()
    max_deque.append(i)
print(test_list[max_deque[0]], end=" ")
