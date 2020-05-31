### without recursion
```python
from math import ceil, log2


def double_search(arr, digit):
    n = 2
    length = len(arr)
    index = length // n
    start = 0
    stop = log2(length)
    while start < stop:
        n **= 2
        start += 1
        if arr[index] > digit:
            index -= ceil(length / n)
        elif arr[index] < digit:
            index += ceil(length / n)
        else:
            return arr[index]
    return "not found"


def main():
	arr = [-2, 0, 1, 2, 4, 5, 6, 8, 10, 14, 16]
	result = double_search(arr, 1)
	print(result)


if __name__ == '__main__':
	main()
```
### recursion implementation
```python
def double_search(arr, digit):
    length = len(arr)
    index = length // 2
    if length == 1 and arr[0] != digit:
        return "not found"
    elif arr[index] < digit:
        return double_search(arr[index:], digit)
    elif arr[index] > digit:
        return double_search(arr[:index], digit)
    else:
        return arr[index]


def main():
	arr = [-2, 0, 1, 2, 4, 5, 6, 8, 10, 14, 16]
	result = double_search(arr, -2)
	print(result)


if __name__ == '__main__':
	main()
```