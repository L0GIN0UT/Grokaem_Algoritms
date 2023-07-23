# Алгоритм Бинарного Поиска/Binar Search Algoritm(B.S.A.)

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

# Алгоритм Быстрой Сортировки/Quick Sort Algoritm(Q.S.A.)

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        start_point = array[0]
        less = [i for i in array[1:] if i <= start_point]
        greater = [i for i in array[1:] if i > start_point]
        return quicksort(less) + [start_point] + quicksort(greater)
    




    
# Поиск в ширину с втроеным примером
## Не для вызова (Индивидульно для каждого раза)

# graph = {}
# graph['You'] = ['Vladimir', 'Artem', 'Vlad', 'Valera']
# graph['Vladimir'] = ['Maria', 'Daniel', 'You']
# graph['Artem'] = ['You', 'Vladimir', 'Daria']
# graph['Vlad'] = ['Anton', 'Valera', 'Andrey']
# graph['Valera'] = ['Ksenia', 'Alexandr', 'Egor']
# graph['Maria'] = []
# graph['Daniel'] = []
# graph['Daria'] = []
# graph['Anton'] = []
# graph['Andrey'] = []
# graph['Ksenia'] = []
# graph['Alexandr'] = []
# graph['Egor'] = []



# print(graph)

# # Поиск в ширину
# from collections import deque


# # проверка на продавца
# def person_is_seller(name):
#     return name[-1] == 'y'


# # Функция поиска
# def search(name):
#     search_queue = deque()
#     search_queue += graph[name]
#     searched = []
#     while search_queue:
#         person = search_queue.popleft()
#         if person not in searched:
#             if person_is_seller(person):
#                 print(person + ' - Продавец Yagermeyster!')
#                 return True
#             else:
#                 search_queue += graph[person]
#                 searched.append(person)
#     return print('Среди вашего окружения нет продавцов Yagermeyster')

# search('You')


# Алгоритм Дейкстры
# Хэш таблица
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['fin'] = 5
graph['fin'] = {}

# Код стоимости
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

# Код родителей
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

# Массив отработанных узлов
processed = []


# node - Узел
def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(processed)




