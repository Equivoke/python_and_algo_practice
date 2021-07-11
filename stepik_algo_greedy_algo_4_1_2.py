"""
Первая строка содержит количество предметов 1≤n≤10^3 и вместимость рюкзака 0≤W≤2*10^6. Каждая из следующих n
строк задаёт стоимость 0≤c_i≤2*10^6 и объём 0≤w_i≤2*10^6. Выведите максимальную стоимость частей предметов
(от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся),
помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.
"""
# Считываем исходные данные и заносим в список цену, количество и цену/количество
amount_of_items, weight_limit = map(int, input().split())
list_of_things = []
for i in range(amount_of_items):
    cost, capacity = map(int, input().split())
    if cost > 0:
        list_of_things.append([cost, capacity, cost/capacity])
# Сортируе список по цена/количество
sorted_list_of_things = sorted(list_of_things, key=lambda x: x[2], reverse=True)
# В цикле добавляем по 1 кг предмета с наибольшей стоимостью пока не кончится предмет или место
current_weight = 0
stored_weight = 0
current_cost = 0
for i in range(len(sorted_list_of_things)):
    if stored_weight < weight_limit:
        while current_weight < sorted_list_of_things[i][1] and current_weight < weight_limit and\
                current_weight + stored_weight < weight_limit:
            current_cost += sorted_list_of_things[i][2]
            current_weight += 1
        stored_weight += current_weight
        current_weight = 0
print(current_cost)
