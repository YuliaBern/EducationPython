#1.Написати програму для обходу графа за алгоритмом пошуку в глибину
#Автор: Бернацька Юлія студентка 31І групи

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")

    for sver in graph[start]:
        if sver not in visited:
            dfs(graph, sver, visited)

# Граф, представлений у вигляді списку суміжності
graph = {
    1: [2, 5, 6],
    2: [1, 3, 6, 5],
    3: [2, 4, 7, 8, 6],
    4: [3, 8, 7, 9],
    5: [1, 6, 2],
    6: [2, 5, 1, 7, 3],
    7: [3, 2, 6, 8, 4],
    8: [3, 7, 4, 9],
    9: [4, 8]
}


dfs(graph, 1)
