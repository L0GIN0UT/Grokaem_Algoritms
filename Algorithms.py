# Алгоритм Бинарного Поиска/Binar Search Algoritm(B.S.A.)

def binary_search(list, item):
    low = 0  # <== Начало массива
    high = len(list) - 1  # <==  # <== Конец массива

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:  # <== Если То что ищем равно Среднему
            return mid
        if guess > item: # <== Если То что ищем меньше Среднего
            high = mid - 1
        else:  # <== Если То что ищем меньше Среднего
            low = mid + 1
    return None

# Алгоритм Быстрой Сортировки/Quick Sort Algoritm(Q.S.A.)

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        start_point = array[0] # <== старт с 1 символа
        less = [i for i in array[1:] if i <= start_point] # <== Перенос влево если меньше чем Старт 
        greater = [i for i in array[1:] if i > start_point] # <== Перенос вправо если больше чем Старт
        return quicksort(less) + [start_point] + quicksort(greater) # <== Возвращаем в массив отсортированных соседей
    




    
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
# from collections import deque # <== Импорт очереди


# # проверка на продавца
# def person_is_seller(name):
#     return name[-1] == 'y'


# # Функция поиска
# def search(name):
#     search_queue = deque() # <== Создаем очередь
#     search_queue += graph[name] # <== Добавляем в очередь Граф
#     searched = [] 
#     while search_queue: # <== Пока очередь не закончится
#         person = search_queue.popleft() # <== Добавляем п роверку крайнего легого из списка очереди
#         if person not in searched: # <== Если он не был обработан
#             if person_is_seller(person): # <== Если он Продавец
#                 print(person + ' - Продавец Yagermeyster!') 
#                 return True
#             else:
#                 search_queue += graph[person] # <== Иначе добавляем его друзей в конец очереди
#                 searched.append(person) # <== Добавляем провереного человека в обработаны
#     return print('Среди вашего окружения нет продавцов Yagermeyster')

# search('You')


# АЛГОРИТМ ДЕЙКСТРЫ
# # Хэш таблица
# graph = {}
# graph['start'] = {}
# graph['start']['a'] = 6
# graph['start']['b'] = 2
# graph['a'] = {}
# graph['a']['fin'] = 1
# graph['b'] = {}
# graph['b']['fin'] = 5
# graph['fin'] = {}

# # Код стоимости
# infinity = float('inf')
# costs = {}
# costs['a'] = 6
# costs['b'] = 2
# costs['fin'] = infinity

# # Код родителей
# parents = {}
# parents['a'] = 'start'
# parents['b'] = 'start'
# parents['fin'] = None

# # Массив отработанных узлов
# processed = []


# # node - Узел
# def find_lowest_cost_node(costs):
#     lowest_cost = float('inf')
#     lowest_cost_node = None
#     for node in costs:  # <== Перебрать все узлы
#         cost = costs[node]
#         if cost < lowest_cost and node not in processed: # <== Если этот узел с наименьщей стоимостью из уже увиденных и он еще не был обработан
#             lowest_cost = cost # <== он назначается узлом с наименьшей стоимостью
#             lowest_cost_node = node
#     return lowest_cost_node


# node = find_lowest_cost_node(costs) # <== Найти узел с наименьшей стоимостью среди необработанных
# while node is not None: # <== Если обработанны все узлы цикл завершается
#     cost = costs[node]
#     neighbors = graph[node]
#     for n in neighbors.keys(): # <== Перебрать всех соседей текущего узла.
#         new_cost = cost + neighbors[n]
#         if costs[n] > new_cost: # <== Если к соседу сожно добраться быстрее добраться через текущий узел
#             costs[n] = new_cost # <== обновить стоимость для этого узла
#             parents[n] = node # <== Этот узел становится новым родителем для соседа
#     processed.append(node) # <== Узел помечается как обработанный
#     node = find_lowest_cost_node(costs) # <== Найти следующий узел для обработки и повторить цикл

# print(processed)
# ['b', 'a', 'fin'] <== ОТВЕТ


# ЖАДНЫЕ АЛГОРИТМЫ / GREED IS GOOD

states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])  # <== Переданный массив преобразует множество

stations = {} # <== Покрытие станций
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

final_stations = set() # <== хранение итогового набора станций

while states_needed: # <== Пока список штатов не станет пустым
    best_station = None # <== Станция которая обслуживает больше всего штатов,
    states_covered = set() 
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station  # <== Пересечение множеств (Входят в оба множества!)
        if len(covered) > len(states_covered):
            best_station = station 
            states_covered = covered
    states_needed -= states_covered # <== Из списка штатов убираем те станции которые входят в зону покрытия
    final_stations.add(best_station) # <== Лучшая станция добавляется в Итоговые станции

print(set(final_stations))
# # {'ktwo', 'kfive', 'kthree', 'kone'} <== ОТВЕТ


## Бинарное дерево
# Обратный обход

# class Node:
#    def __init__(self, data):
#       self.left = None
#       self.right = None
#       self.data = data
# # Insert Node
#    def insert(self, data):
#       if self.data:
#          if data < self.data:
#             if self.left is None:
#                self.left = Node(data)
#             else:
#                self.left.insert(data)
#          elif data > self.data:
#             if self.right is None:
#                self.right = Node(data)
#             else:
#                self.right.insert(data)
#       else:
#          self.data = data
# # Print the Tree
#    def PrintTree(self):
#       if self.left:
#          self.left.PrintTree()
#       print( self.data),
#       if self.right:
#          self.right.PrintTree()
# # Inorder traversal
# # Left -> Root -> Right
#    def inorderTraversal(self, root):
#       res = []
#       if root:
#          res = self.inorderTraversal(root.left)
#          res.append(root.data)
#          res = res + self.inorderTraversal(root.right)
#       return res
# root = Node(27)
# root.insert(14)
# root.insert(35)
# root.insert(10)
# root.insert(19)
# root.insert(31)
# root.insert(42)
# print(root.inorderTraversal(root)) 

# [10, 14, 19, 27, 31, 35, 42]

# Прямой обход

# class Node:
#    def __init__(self, data):
#       self.left = None
#       self.right = None
#       self.data = data
# # Insert Node
#    def insert(self, data):
#       if self.data:
#          if data < self.data:
#             if self.left is None:
#                self.left = Node(data)
#             else:
#                self.left.insert(data)
#          elif data > self.data:
#             if self.right is None:
#                self.right = Node(data)
#             else:
#                self.right.insert(data)
#          else:
#             self.data = data
# # Print the Tree
#    def PrintTree(self):
#       if self.left:
#          self.left.PrintTree()
#       print( self.data),
#       if self.right:
#          self.right.PrintTree()
# # Preorder traversal
# # Root -> Left ->Right
#    def PreorderTraversal(self, root):
#       res = []
#       if root:
#          res.append(root.data)
#          res = res + self.PreorderTraversal(root.left)
#          res = res + self.PreorderTraversal(root.right)
#       return res
# root = Node(27)
# root.insert(14)
# root.insert(35)
# root.insert(10)
# root.insert(19)
# root.insert(31)
# root.insert(42)
# print(root.PreorderTraversal(root))

# [27, 14, 10, 19, 35, 31, 42]

# Центрированный обход

# class Node:
#     def __init__(self, data):
#         self.left = None
#         self.right = None
#         self.data = data
# # Insert Node
#     def insert(self, data):
#         if self.data:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insert(data)
#             elif data > self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#         else:
#             self.data = data
# # Print the Tree
#     def PrintTree(self):
#         if self.left:
#             self.left.PrintTree()
#         print(self.data),
#         if self.right:
#             self.right.PrintTree()
# # Postorder traversal
# # Left ->Right -> Root
#     def PostorderTraversal(self, root):
#         res = []
#         if root:
#             res = self.PostorderTraversal(root.left)
#             res = res + self.PostorderTraversal(root.right)
#             res.append(root.data)
#         return res
# root = Node(27)
# root.insert(14)
# root.insert(35)
# root.insert(10)
# root.insert(19)
# root.insert(31)
# root.insert(42)
# print(root.PostorderTraversal(root))

# [10, 19, 14, 31, 42, 35, 27]

## Создание инвертированного индекса
# Открываем файл
# class Invert:
#     file = open('file.txt', encoding='utf8')
#     read = file.read()
#     file.seek(0)
#     read
    
#     # чтобы получить
#     # количество строк
#     # в файле
#     line = 1
#     for word in read:
#         if word == '\n':
#             line += 1
#     print("Строк в файле: ", line)
    
#     # создайте список для
#     # сохранения каждой строки в виде
#     # элемента списка
#     array = []
#     for i in range(line):
#         array.append(file.readline())
    
#     array
#     # Строк в файле:  3

#     # Удалите знаки препинания: 
#     punctuation = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
#     for element in read: 
#         if element in punctuation: 
#             read = read.replace(element, " ")         
#     read
    
#     # для поддержания однородности
#     read = read.lower()                   
#     read
#     #'this is the first word \n
#     #this is the second text hello how are you \n
#     #this is the third this is it now '

#     # Обозначение данных в виде отдельных слов:
#     def tokenize_words(file_contents):
#         #Маркирует содержимое файла.
#             #Параметры
#             #----------
#             #file_contents : список
#             #Список строк, содержащих содержимое файла.
#             #
#             #Возвращается
#             #-------
#             #Список строк, содержащих содержимое помеченного файла.         
#         result = []
    
#         for i in range(len(file_contents)):
#             tokenized = []
#             # print("Строка есть", file_contents[i])
#             # разделите строку пробелами
#             tokenized = file_contents[i].split()
#             result.append(tokenized)
#         return result
    
#     # Очистка данных, удаление стоп-слова:
#     from nltk.tokenize import word_tokenize
#     import nltk
#     from nltk.corpus import stopwords
#     nltk.download('stopwords')
 
#     for i in range(1):
#         # Это преобразует
#         # Слова в токены
#         text_tokens = word_tokenize(read)
    
#     tokens_without_sw = [
#         word for word in text_tokens if not word in stopwords.words()]
    
#     print(tokens_without_sw)
#     #['first', 'word', 'second', 'text', 'hello', 'third']

#     # Создание инвертированного индекса:
#     dict = {}
 
#     for i in range(line):
#         check = array[i].lower()
#         for item in tokens_without_sw:
    
#             if item in check:
#                 if item not in dict:
#                     dict[item] = []
    
#                 if item in dict:
#                     dict[item].append(i+1)
#     dict
#         #{'first': [1],
#         #'word': [1],
#         #'second': [2], 
#         #'text': [2], 
#         #'hello': [2], 
#         #'third': [3]}

