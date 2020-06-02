### Поиск в ширину
```python
from queue import Queue # fifo


def BFS(edges, start):
    '''breadth-first search'''
    result = {key:None for key in edges}
    result[start] = 0
    q = Queue()
    q.put(start)
    marked_points = set()
    marked_points.add(start)
    while not q.empty():
        point = q.get()
        for n in edges[point]:
            if n not in marked_points:
                result[n] = result[point] + 1
                marked_points.add(n)
                q.put(n)
    return result


def main():
    edges = {
        "S":["A", "B"],
        "A":["S", "C"],
        "B":["S", "C", "D"],
        "C":["A", "B", "D", "E"],
        "D":["C", "B", "E"],
        "E":["C", "D"]
    }
    start = "S"
    result = BFS(edges, start)
    print(result)


if __name__ == '__main__':
    main()
```
### Нахождение связанных компонент
```python
def serachUCC(edges):
    '''unique connect component'''
    all_point = set(edges.keys())
    count = 0
    while all_point:
        next_point = all_point.pop()
        result = BFS(edges, next_point)
        result = set(filter(result.get, result))
        all_point -= result
        count += 1
    return count


def main():
    edges = {
    "A":["B", "C"],
    "B":["C", "A"],
    "C":["A","B","D","E"],
    "D":["C"],
    "E":["C"],
    "F":["G"],
    "G":["F"],
    "H":["M"],
    "M":["N", "H"],
    "N":["M"],
    }
    result = serachUCC(edges)
    print(result)


if __name__ == '__main__':
    main()
```