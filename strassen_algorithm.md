
```python
from math import log2, ceil
from random import randint


def expand_matrix(a, length):
    expand_length = ceil(log2(length))
    expand_length = 2 ** expand_length
    for row in a:
        while len(row) < expand_length:
            row.append(0)
    while len(a) < expand_length:
        a.append([0 for i in range(expand_length)])
    return a


def add(a, b):
    return [[s + f for s, f in zip(*i)] for i in zip(a, b)]


def sub(a, b):
    return [[s - f for s, f in zip(*i)] for i in zip(a, b)]


def merge_two_matrix(a, b):
    for i, j in zip(a, b):
            i.extend(j)
            

def mul_matrix(a, b):
    if len(a) > 2:
        length = len(a) // 2
        atl = [i[:length] for i in a][:length]
        abl = [i[:length] for i in a][length:]
        atr = [i[length:] for i in a][:length]
        abr = [i[length:] for i in a][length:]

        btl = [i[:length] for i in b][:length] # tl
        bbl = [i[:length] for i in b][length:] # bl
        btr = [i[length:] for i in b][:length] # tr
        bbr = [i[length:] for i in b][length:] # br
        
        p1 = mul_matrix(add(atl, abr), add(btl, bbr))
        p2 = mul_matrix(add(abl, abr), btl)
        p3 = mul_matrix(atl, sub(btr, bbr))
        p4 = mul_matrix(abr, sub(bbl, btl))
        
        p5 = mul_matrix(add(atl, atr), bbr)
        p6 = mul_matrix(sub(abl, atl), add(btl, btr))
        p7 = mul_matrix(sub(atr, abr), add(bbl, bbr))
        
        rtl = add(sub(add(p1, p4), p5), p7)
        rtr = add(p3, p5)
        rbl = add(p2, p4)
        rbr = add(add(sub(p1, p2), p3), p6)

        merge_two_matrix(rtl, rtr)
        merge_two_matrix(rbl, rbr)
    
        rtl.extend(rbl)
        result = rtl
    else:
        result = [
            [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]],
        ]
    return result


def dot_matrix(a, b):
    lengthes = [len(a), len(b), len(a[0]), len(b[0])]
    log2_lengthes = [log2(i) for i in lengthes]
    is_integer_log2_lengthes = [i.is_integer() for i in log2_lengthes]
    same_lengthes = [lengthes[0] == lengthes[i] for i in range(1, 4)][0]
    if not all([*is_integer_log2_lengthes, same_lengthes]):
        max_length = max(lengthes)
        a = expand_matrix(a, max_length)
        b = expand_matrix(b, max_length)
    result = mul_matrix(a, b)
    result = [i[:lengthes[-1]] for i in result][:lengthes[0]]
    return result


def main():
	rows, cols = (8, 5)
	A = [[randint(-5, 10) for i in range(cols)] for i in range(rows)]
	rows, cols = (5, 8)
	B = [[randint(-5, 10) for i in range(cols)] for i in range(rows)]
	result = dot_matrix(A, B)
	print(*result, sep="\n")


if __name__ == '__main__':
	main()
```