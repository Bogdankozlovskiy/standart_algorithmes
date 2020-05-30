### Karatsuba multiply
<img src="https://render.githubusercontent.com/render/math?math=\overline{ab} \cdot \overline{cd}=">
<img src="https://render.githubusercontent.com/render/math?math=\overline{ab} \cdot \overline{cd}=">
<img src="https://render.githubusercontent.com/render/math?math=(a\cdot 10 + b)\cdot(c\cdot 10 + d)=">
<img src="https://render.githubusercontent.com/render/math?math=a\cdot c \cdot 100 + a\cdot d \cdot 10 + b\cdot c\cdot 10 + b\cdot d=">
<img src="https://render.githubusercontent.com/render/math?math=a\cdot c \cdot 100 + (a\cdot d + b\cdot c)\cdot 10 + b\cdot d=">
<img src="https://render.githubusercontent.com/render/math?math=a\cdot c \cdot 100 + ((a + b)\cdot(c + d) - a\cdot c - b\cdot d)\cdot 10 + b\cdot d">

```python
from math import log2, ceil


def preprocess_digit(first, second):
    length_first = ceil(log2(len(first)))
    length_second = ceil(log2(len(second)))
    length = max(length_first, length_second)
    length = 2 ** length
    while len(first) < length:first.insert(0, 0)
    while len(second) < length:second.insert(0, 0)
    return length


def karatsuba(first, second, length):
    if len(first) == len(second) == 1:
        return first[0] * second[0]
    a = first[:length]
    b = first[length:]
    c = second[:length]
    d = second[length:]
    ac = karatsuba(a, c, length // 2)
    bd = karatsuba(b, d, length // 2)
    a_plus_b = [sum(i) for i in zip(a, b)]
    d_plus_c = [sum(i) for i in zip(d, c)]
    abcd = karatsuba(a_plus_b, d_plus_c, length // 2)
    return ac * 10 ** (2 * length) + (abcd - ac - bd) * 10 ** length + bd


def multiply(first, second):
    length = preprocess_digit(first, second)
    return karatsuba(first, second, length // 2)
    

def main():
    first_digit = [5, 1, 6]
    second_digit = [7, 3]
    result = multiply(first_digit, second_digit)
    print(result)


if __name__ == "__main__":
    main()
```
