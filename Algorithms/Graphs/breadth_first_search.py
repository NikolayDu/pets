# breadth-first search - поиск в ширину

# Решает такие вопросы, как:
#   1) существует ли путь от узла А к узлу Б
#   2) как выглядит кратчайший путь от узла А к узлу Б

# Complexity: 0(Количество людей + количество ребер). Обычно записывается 0(V+E), где V - количество вершин,
# E - количество ребер


# deque - двусторонняя очередь

from collections import deque


def person_is_seller(name):
    return name[-1] == "m"

def is_mango_seller(name):

    search_queue = deque()  # Создание новой очереди
    search_queue += graph[name]  # Все соседи добавляются в очередь поиска
    searched = []   # Массив для отслеживания уже проверенных имен

    while search_queue:     # Пока очередь не пуста...
        person = search_queue.popleft()     # Из очереди извлекается первый человек
        if person not in searched:      # Человек проверяется только если он не входит в список проверенных ранее
            if person_is_seller(person):    # Проверяем является ли этот человек продавцом манго
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]   # Если же человек не является продавцом,
                                                # то все его друзья добавляются в очередь поиска
                searched.append(person)     # Добавляем человека, как уже проверенного.



    return False    # Если выполнение дошло до этой строки, значит, в очереди нет продавца манго

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


is_mango_seller("you")