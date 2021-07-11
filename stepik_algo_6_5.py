"""
Задача на программирование: точки и отрезки

В первой строке задано два целых числа 1≤n≤50000 и 1≤m≤50000 — количество отрезков и точек на прямой, соответственно.
Следующие n строк содержат по два целых числа a_i и b_i (a_i≤b_i) — координаты концов отрезков.
Последняя строка содержит m целых чисел — координаты точек. Все координаты не превышают 10^8 по модулю.
Точка считается принадлежащей отрезку, если она находится внутри него или на границе.
Для каждой точки в порядке появления во вводе выведите, скольким отрезкам она принадлежит.
"""
import bisect

# Считываем исходные данные
n_m_list = list(map(int, input().split()))
n, m = n_m_list[0], n_m_list[1]
list_of_segments = [list(map(int, input().split())) for _ in range(n)]
list_of_dots = list(map(int, input().split()))
# Разбиваем список с отрезками на 2: список "начал" и список "концов" отрезков. Сортируем их для последующего поиска
sorted_by_left = [x[0] for x in list_of_segments]
sorted_by_left.sort()
sorted_by_right = [x[1] for x in list_of_segments]
sorted_by_right.sort()
# Для подсчёта количества отрезков, которым принадлежит точка вычислим разность между N и M
for dot in list_of_dots:
    # Осуществим поиск в массиве "начал" количества элементов, которые меньше или равны проверяемой точке
    # для этого воспользуемся бинарным поиском bisect_right
    cntr_left = 0
    cntr_left += bisect.bisect_right(sorted_by_left, dot)
    # Осуществим поиск в массиве "концов" количества элементов, которые строго меньше проверяемой точки
    # для этого воспользуемся бинарным поиском bisect_left
    cntr_right = 0
    cntr_right += bisect.bisect_left(sorted_by_right, dot)
    fin_cntr = cntr_left - cntr_right
    print(fin_cntr, end=" ")
