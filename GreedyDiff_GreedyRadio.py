def get_cost(t):
    time = 0
    score = 0
    for i in t:
        time += i[1]
        score += time * i[0]
    return score


def GreedyDiff(t):
    return sorted(t, key=lambda item: -(item[0] - item[1]))


def GreedyRatio(t):
    return sorted(t, key=lambda item: -(item[0] / item[1]))


def main():
    tasks = [(1, 2), (2, 1), (5, 4), (7, 2), (2, 7), (4, 5)] # w, t
    # we needed to sorted this task by decresses cost parameter
    print(f"mark for random task sequence {get_cost(tasks)}")
    diff_sequence = GreedyDiff(tasks)
    print(f"mark for GreedyDiff sequence  {get_cost(diff_sequence)}")
    ratio_sequence = GreedyRatio(tasks)
    print(f"mark for GreedyRatio sequence {get_cost(ratio_sequence)}")


if __name__ == "__main__":
    main()