from random import randint


def split_array(arr, length):
    index = length // 2
    suport = arr[index]
    left = []
    middle = []
    right = []
    for digit in arr:
        if digit < suport:
            left.append(digit)
        elif digit == suport:
            middle.append(digit)
        else:
            right.append(digit)
    return left, middle, right


def double_serch_order(arr, order):
    length = len(arr)
    assert length >= order, "order must be less then length arr"
    left, middle, right = split_array(arr, length) 
    if len(left) >= order:
        return double_serch_order(left, order)
    elif len(left) + len(middle) < order:
        return double_serch_order(right, order - len(left) - len(middle))
    else:
        return middle
    

def main():
    length_arr = 100
    arr = [randint(-50, 50) for i in range(100)]
    median = length_arr // 2
    lower_quartile = length_arr // 4
    upper_quartile = length_arr // 4 * 3
    print(f"median is {double_serch_order(arr, median)}")
    print(f"lower quartile is {double_serch_order(arr, lower_quartile)}")
    print(f"upper quartile is {double_serch_order(arr, upper_quartile)}")
    

if __name__ == '__main__':
    main()