"""
Бираный поиск
"""
def binary_search(my_list, item):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low + high)
        guess = my_list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


"""
Сортировка выбором
"""
def find_smallest(my_list):
    smallest = my_list[0]  # saving smallest val
    smallest_ind = 0  # saving index of smallest val
    for i in range(1, len(my_list)):
        if my_list[i] < smallest:
            smallest = my_list[i]
            smallest_ind = i
    return smallest_ind

def selection_sort(mylist):
    tmp_list = []
    for i in range(len(mylist)):
        smallest = find_smallest(mylist)  # Find smallest elem in mylist, add it to tmp_list and remove from mylist
        tmp_list.append(mylist.pop(smallest))
    return tmp_list

"""
Быстрая сортировка массива
"""
def qsort(test_list):
    if len(test_list) < 2:
        return test_list  # базовый случай, массивы из 0 и 1 элементов уже "отсортированы"
    else:
        pivot = test_list[0]  # опорный элемент
        less = [i for i in test_list[1:] if i <= pivot]  # подмассив всех элементов, меньше опорного
        greater = [i for i in test_list[1:] if i > pivot]
        return qsort(less) + [pivot] + qsort(greater)

"""
BFS | Поиск в ширину
"""
from collections import deque
# Граф из моиз друзей и друзей их друзей
graph = {"you": ["alice", "ЬoЬ", "claire"], "ЬoЬ": ["anuj", "peggy"], "alice": ["peggy"], "claire": ["thom", "Mango"],
         "anuj": [], "peggy": [], "thom": [], "Mango": []}
# Проверяем, продаёт ли человек манго
def person_is_seller(name):
    return name == 'Mango'
def search_mango_seller(name):
    search_queue = deque()
    search_queue += graph[name]  # Записываем всех друзей человека в очередь
    cheked_ppls = []  # Список, чтобы не проверять одного человека 2 раза
    while search_queue:
        person = search_queue.popleft()  # Берём левого человека из очереди и проверяем
        if person not in cheked_ppls:
            if person_is_seller(person):  # Проверяем, продавец ли
                print(person + ' is seller!')
                return True
            else:  # Т.к. не продавец - добавляем его друзей в очередь и помещаем его самого в список проверенных
                search_queue += graph[person]
                cheked_ppls.append(person)
    return False
search_mango_seller('you')