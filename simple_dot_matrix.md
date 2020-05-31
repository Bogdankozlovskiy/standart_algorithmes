### Simple Algorith multiply matrix
![](https://github.com/Bogdankozlovskiy/standart_algorithmes/blob/master/images/matrix multiply.jpg)

```python
from math import log2, ceil
from random import randint


def get_ranfom_matrix(rows, cols):
    return [[randint(-5, 10) for i in range(cols)] for i in range(rows)]


def expand_matrix(a, length):
    expand_length = ceil(log2(length))
    expand_length = 2 ** expand_length
    for row in a:
        while len(row) < expand_length:
            row.append(0)
    while len(a) < expand_length:
        a.append([0 for i in range(expand_length)])
    return a


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
        
        p1 = mul_matrix(atl, btl)
        p2 = mul_matrix(atr, bbl)
        p3 = mul_matrix(atl, btr)
        p4 = mul_matrix(atr, bbr)
        
        p5 = mul_matrix(abl, btl)
        p6 = mul_matrix(abr, bbl)
        p7 = mul_matrix(abl, btr)
        p8 = mul_matrix(abr, bbr)
        
        b1 = [[sum(j) for j in zip(*i)] for i in zip(p1, p2)] # p1 + p2
        b2 = [[sum(j) for j in zip(*i)] for i in zip(p3, p4)] # p3 + p4
        b3 = [[sum(j) for j in zip(*i)] for i in zip(p5, p6)] # p5 + p6
        b4 = [[sum(j) for j in zip(*i)] for i in zip(p7, p8)] # p7 + p8
        
        for i, _ in enumerate(b1):
            b1[i].extend(b2[i])
            b3[i].extend(b4[i])
        b1.extend(b3)
        return b1
    else:
        result = [
            [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]],
        ]
    return result


def dot_matrix(a, b):
    lengthes = [len(a), len(b), len(a[0]), len(b[0])]
    assert lengthes[1] == lengthes[2], "both matrix must be have same sizes"
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
	A = get_ranfom_matrix(9, 5)
	B = get_ranfom_matrix(5, 7)
	result = dot_matrix(A, B)
	print(*result, sep="\n")


if __name__ == "__main__":
	main()
```
