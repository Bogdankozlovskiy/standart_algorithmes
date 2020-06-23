import heapq


class Node:
    def __init__(self, count:int, letter=None, left=None, right=None):
        self.count = count
        self.letter = letter
        self.left = left
        self.right = right
    
    def get_letter(self, code:str) -> Node:
        cursore = self
        for i in code:
            if i == "1":
                cursore = cursore.right or None
            else:
                cursore = cursore.left or None
            if cursore is None:
                return None
        return cursore
    
    def pprint(self, pref=""):
        if self.letter is not None:
            print(self.letter, pref)
        if self.left is not None:
            self.left.pprint(pref + "0")
        if self.right is not None:
            self.right.pprint(pref + "1")
    
    def __lt__(self, other:Node) -> bool:
        return self.count < other.count
        

def hufman(list_frequency:list) -> Node:
    list_frequency = [Node(*value) for value in list_frequency]
    heapq.heapify(list_frequency)
    while len(list_frequency) > 1:
        f = heapq.heappop(list_frequency)
        s = heapq.heappop(list_frequency)
        n = Node(f.count + s.count, left=f, right=s)
        heapq.heappush(list_frequency, n)
    return list_frequency[0]


def main():
    task = [(3, "A"), (2, "B"), (6, "C"), (8, "D"), (2, "E"), (6, "F")]    
    res = hufman(task)
    res.pprint()
    A = res.get_letter("100").letter
    print()
    print(f"result of res.get_letter('100').letter is {A}")
    
    
if __name__ == "__main__":
    main()