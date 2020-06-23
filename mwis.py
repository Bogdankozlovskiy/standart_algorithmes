__doc__ = """необходимо найти несвязанное множество с наибольшей суммой"""


def wis(grp):
    resul = [0, grp[0]]
    for n in grp[1:]:
        resul.append(max(resul[-1], resul[-2] + n))
    return resul


def wis_reconstruction(win_res, grp):
    result = []
    index = len(grp) - 1
    while index >= 0:
        if win_res[index] >= win_res[index - 1] + grp[index]:
            index -= 1
        else:
            result.append(grp[index])
            index -= 2
    return result[::-1]


def mwis(grp):
    if len(grp) < 2:
        return grp
    first = mwis(grp[:-1])
    second = mwis(grp[:-2]) + grp[-1:]
    if sum(first) > sum(second):
        return first
    return second


def main():
	graph = [3, 2, 1, 6, 4, 5]
	out = wis(graph)
	print(out)
	print(wis_reconstruction(out, graph))
	print("reccursion solve")
	print(mwis(graph))


if __name__ == '__main__':
	main()
