# Задача: найти вершину, путь к которой лежит через вершины 1, 5 и 2

def dfs(v, data):
    if v in graph.keys() and (v == 1 or v == 5 or v == 2):
        data.append(v)
        for u in graph[v]:
            dfs(u, data)
    elif v not in graph.keys() and data == [1, 5, 2]:
        print(v)


# Задача: найти уровень дерева, на котором сумма весов наибольшая

def bfs(v):
    first = [v]
    second = []
    maximum = 0
    max_level = 0
    current_level = 1
    while True:
        for u in first:
            if u in graph.keys():
                for elem in graph[u]:
                    second.append(elem)
        current_level += 1
        if sum(second) > maximum:
            maximum = sum(second)
            max_level = current_level
        if not second:
            break
        first, second = second, []

    print("Максимальная сумма", maximum, "находится на уровне номер", max_level)


graph = {
    1: [5, 3],
    5: [2, 6],
    3: [8, 4],
    2: [9],
    6: [0],
    8: [7],
    4: [10]
}

print("Номер вершины")
dfs(1, [])
print()
bfs(1)

