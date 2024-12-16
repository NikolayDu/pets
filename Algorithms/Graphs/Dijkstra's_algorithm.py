#   Алгоритм Дейкстры
# Если же поиск в ширину находит путь с минимальным количеством сегментов (ребер) (в невзвешенном графе), то
# Алгоритм Дейкстры ищет самый быстрый путь с минимальными весами ребер (во взвешенном графе).


# !!! Алгоритм Дейкстры работает только с направленными ациклическими графами. Так же он
# не будет правильно работать, если у реберт есть отрицательные веса (тут уже нужен будет алгоритм Беллмана-Форда)


# ГРАФ
graph = {}

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}   # У конечного узла нет соседей

# Таблица стоимостей
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# Таблица родителей
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []  # Массив для отслеживания всех уже обработанных узлов,
                # т.к. один узел не должен обрабатываться многократно

# node - узел
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:  # Перебираем все узлы
        cost = costs[node]
        if cost < lowest_cost and node not in processed:    # Если это узел с наименьшей стоимостью из уже
                                                            # увиденных и он ещё не был обработан...
            lowest_cost = cost  # ...он назначается новым узлом с наименьшей стоимостью
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs) # Находим узел с наименьшей стоимостью среди необработанных
while node is not None: # Если обработаны все узлы, цикл while завершен
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():  # Перебрать всех соседей текущего узла
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:  # Если к соседу можно быстрее добраться через текущий узел...
            costs[n] = new_cost     # ... обновить стоимость для этого узла
            parents[n] = node   # Этот узел становится новым родителем для соседа
    processed.append(node)  # Узел помечается как обработанный
    node = find_lowest_cost_node(costs)  # Найти следующий узел для обработки и повторить цикл


# Выводим стоимость до "Конца"
print(costs["fin"])