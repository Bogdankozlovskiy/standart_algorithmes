from random import randint


def merge_sort(arr):
    length = len(arr)
    if length < 2:
        return arr
    length //= 2
    left = merge_sort(arr[:length])
    right = merge_sort(arr[length:])
    out = []
    while left and right:
        if left[0] > right[0]:
            out.append(right.pop(0))
        else:
            out.append(left.pop(0))
    out.extend(left)
    out.extend(right)
    return out


def main():
    arr = [randint(-5, 5) for i in range(10)]
    print(arr)
    result = merge_sort(arr)
    print(result)
    

if __name__ == "__main__":
    main()