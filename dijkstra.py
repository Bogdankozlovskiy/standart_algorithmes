roads = {
    "A":{"B":3, "E":6, "D":5},
    "B":{"A":3, "E":2, "C":2},
    "D":{"A":5, "E":4},
    "E":{"A":6, "B":2, "D":4, "C":2, "K":6, "Z":3},
    "C":{"B":2, "E":2, "F":5},
    "Z":{"E":3, "K":4},
    "K":{"E":6, "F":2, "M":2, "Z":4},
    "F":{"C":5, "K":2, "M":1},
    "M":{"F":1, "K":2}
}

def dijkstra(start, finish, roads):
    result = {key:float("inf") for key in roads.keys()}
    edges = set()
    result[start] = 0

    while finish not in edges:
        node = min(result, key=lambda x: float("inf") if x in edges else result[x])
        edges.add(node)
        for neighbor in roads[node]:
            length = roads[node][neighbor] + result[node]
            if length < result[neighbor]:
                result[neighbor] = length

    return result


def main():
	start = "A"
	finish = "M"
	result = dijkstra(start, finish, roads)
	print(result)


if __name__ == "__main__":
	main()