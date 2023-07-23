# Test
# Задача: Среди 'друзей' и друзей 'друзей' найдите продавца Yagermeyster
# Продавцом Yagermeyster является человек чье имя заканчивается буквой Y

graph = {}
graph['You'] = ['Vladimir', 'Artem', 'Vlad', 'Valera']
graph['Vladimir'] = ['Maria', 'Daniel', 'You']
graph['Artem'] = ['You', 'Vladimir', 'Daria']
graph['Vlad'] = ['Anton', 'Valera', 'Andrey']
graph['Valera'] = ['Ksenia', 'Alexandr', 'Egor']
graph['Maria'] = []
graph['Daniel'] = []
graph['Daria'] = []
graph['Anton'] = []
graph['Andrey'] = []
graph['Ksenia'] = []
graph['Alexandr'] = []
graph['Egor'] = []



print(graph)

# Поиск в ширину
from collections import deque


# проверка на продавца
def person_is_seller(name):
    return name[-1] == 'y'


# Функция поиска
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + ' - Продавец Yagermeyster!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return print('Среди вашего окружения нет продавцов Yagermeyster')

search('You')


# ХЭШ-ТАБЛИЦА (словарь)

# book = dict()
#
# book['apple'] = 0.67
# book['milk'] = 1.49
# book['avocado'] = 1.49
# book['orange'] = 0.86
# book['cheese'] = 3.02
# print(book)
# # {'apple': 0.67, 'milk': 1.49, 'avocado': 1.49, 'orange': 0.86, 'cheese': 3.02}
# print(book['avocado'])
# # 1.49



#  РЕКУРСИЯ
# сравнение с циклом while
# задача: есть ящик с замком. ключ от этого ящика лежит
# в коробке в которой много коробок (в коробках могут быть другие коробки)
# найдите ключ


# ПСЕВДОКОД - буквально написанно что делает
# pile - куча
# Цикл WHILE
# def look_for_key(main_box):
#     pile = main_box.make_a_pile_to_look_through()
#     while pile is not empty:
#         box = pile.grab_a_box()
#         for item in box():
#             if item.is_a_box():
#                 pile.append(item)
#             elif item.is_a_key():
#                 print("found the key !")

# РЕКУРСИЯ
# def look_for_key(box):
#     for item in box:
#         if item.is_a_box():
#             look_for_key(item)
#         elif item.is_a_key():
#             print("found the key !")

# Рекурсия занимает меньшн места !!!



# Алгоритм сортироки (медленный)
# (2 метода) поиск наименьшего значения
# метод сортировки
# Учитываем какой вид доступа (последовательный/произвольный)
# последовательный - используем списки (в предыдущем хранится инф.
# о следующем но ХРАНЯТСЯ они в РАЗНЫХ местах)
# произвольный - импользуем массивы
# (все эл. хранятся рядом друг с другом)
# Массивы используют ТОЛЬКО ОДНОТИПНЫЙ вид данных

# def findSmallest(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(0, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index


# # .pop - фозвращает значение элемент с индексом i
# # и удаляет его из начального массива
# def selectionSor(arr):
#     newArr = []
#     for i in range(0, len(arr)):
#         smallest = findSmallest(arr)
#         newArr.append(arr.pop(smallest))
#     return newArr


# # print(selectionSor([5,3,6,2,10]))
# # print(sorted([5,3,6,2,10]))