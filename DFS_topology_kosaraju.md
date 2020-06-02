### Поиск в глубину
```python
from queue import deque # lifo


def DFS(graph, marked_points, start):
    '''depth-first search'''
    d = deque()
    d.append(start)
    marked_points.add(start)
    while d:
        point = d.pop()
        flag = True
        for n in graph[point]:
            if n not in marked_points:
                flag = False
                marked_points.add(n)
                d.append(n)
        if flag:
            return point


def main():
    graph = {
        "S":["A", "B"],
        "A":["S", "C"],
        "B":["S", "C", "D"],
        "C":["A", "B", "D", "E"],
        "D":["C", "B", "E"],
        "E":["C", "D"]
    }
    marked_points = set()
    start = "S"
    result = DFS(graph, marked_points, start)
    print(result)


if __name__ == '__main__':
    main()
```
### Поиск в глубину используя рекурсию
```python
def DFS(graph, marked_points, start):
    '''depth-first search'''
    marked_points.add(start)
    for n in graph[start]:
        if n not in marked_points:
            return DFS(graph, marked_points, n)
    return start


def main():
    graph = {
        "S":["A", "B"],
        "A":["S", "C"],
        "B":["S", "C", "D"],
        "C":["A", "B", "D", "E"],
        "D":["C", "B", "E"],
        "E":["C", "D"]
    }
    marked_points = set()
    start = "S"
    result = DFS(graph, marked_points, start)
    print(result)


if __name__ == '__main__':
    main()
```
### Нахождение топологии графа. топология отвечает на вопрос "в какой последовательности лучше обходить не направленыый граф чтоб посетить максимальное колличество узлов?"
```python
def topology_sort(graph):
    best_result = {}
    for p in graph:
        result = {}
        count = len(graph)
        while count:
            marked_nodes = set(result.keys())
            node = DFS(graph, marked_nodes, p)
            result[node] = count
            count -= 1
        if len(result) > len(best_result):
            best_result = result
    return best_result


def main():
    graph = {
        "S":["V", "W"],
        "V":["T"],
        "W":["T"],
        "T":[]
    }
    result = topology_sort(graph)
    print(result)


if __name__ == '__main__':
    main()
```
### Нахождение сильно связанных компонент. другими словами нахождение цикличных участков ацикличного графа.
так-же он известен как олгаритм Косараджу.
```python
def reverse_graph(graph):
    new_graph = {}
    for key in graph:
        for n in graph[key]:
            if n not in new_graph:
                new_graph[n] = [key]
            else:
                new_graph[n].append(key)
    return new_graph


def kosaraju(graph):
    reversed_edges = reverse_graph(graph)
    topology_sort_reversed_edges = topology_sort(reversed_edges)
    sorted_points = sorted(topology_sort_reversed_edges, key=topology_sort_reversed_edges.get)
    count = 0
    marked = set()
    for point in sorted_points:
        if point not in marked:
            count += 1
            searchDFS(graph, marked, point)
    return count


def main():
    graph = {
        "A":["C"],
        "B":["D", "H"],
        "C":["E", "L"], 
        "D":["G"],
        "E":["A", "G", "M"],
        "F":["N"],
        "G":["M"],
        "H":["F"],
        "M":["B", "D", "H"],
        "N":["H"],
        "L":["F", "H"],
    }
    result = kosaraju(graph)
    print(result)


if __name__ == '__main__':
    main()
```