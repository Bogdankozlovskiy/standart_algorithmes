import heapq
__doc__ = """минимальные остовные деревья"""

def kraskal(grp):
    heapq.heapify(grp)
    left = {"A"}
    way = []
    result = 0
    while grp:
        edg = heapq.heappop(grp)
        if (edg[1][0] not in left) or (edg[1][1] not in left):
            result += edg[0]
            left.add(edg[1][0])
            left.add(edg[1][1])
            way.append(edg[1])
    return result, way


def prim(grp):
    left = set(grp.keys())
    neigh = left.pop()
    right = list((i[1], i[0], i[0] + neigh) for i in grp[neigh].items())
    heapq.heapify(right)
    result = 0
    way = []
    while left:
        item = heapq.heappop(right)
        while item[1] not in left:
            item = heapq.heappop(right)
        left.remove(item[1])
        result += item[0]
        way.append(item[-1])
        for i in grp[item[1]].items():
            heapq.heappush(right, (i[1], i[0], i[0] + item[1]))
    return result, way


def main():
    print("kraskal")
    graph = [(1, 'AB'), (3, 'AD'), (4, 'AC'), (2, 'BD'), (5, 'DC')]
    print(kraskal(graph))
    print("prima")
    graph = {
        "A":{"B":1, "D":3, "C":4},
        "B":{"A":1, "D":2},
        "D":{"A":3, "B":2, "C":5},
        "C":{"A":4, "D":5}
    }
    print(prim(graph))
    

if __name__ == "__main__":
    main()