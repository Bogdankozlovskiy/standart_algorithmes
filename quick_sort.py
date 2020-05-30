from random import randint


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    suport = arr[0]
    left = []
    right = []
    middle = []
    for i in arr:
        if i < suport:
            left.append(i)
        elif i == suport:
            middle.append(i)
        else:
            right.append(i)
    return quick_sort(left) + middle + quick_sort(right)


def main():
    arr = [randint(-5, 5) for i in range(10)]
    print(arr)
    result = quick_sort(arr)
    print(result)


if __name__ == "__main__":
    main()