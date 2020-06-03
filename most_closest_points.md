### recursion fun for find two the most closest points
+ asymptotics is n*log(n)
<img src="https://latex.codecogs.com/svg.latex?\Large&space;n\cdot log(n)"/>

```python
from math import sqrt
from random import randint


def find_distance(first, second):
    x_delta = first[0] - second[0]
    y_delta = first[1] - second[1]
    return sqrt(x_delta ** 2 + y_delta ** 2)


def find_distance_point_arr(point, arr):
    min_distance = float("inf")
    a = None
    for p in arr:
        distance = find_distance(point, p)
        if distance < min_distance:
            min_distance = distance
            a = p
    return min_distance, a, point


def find_most_closest_points(arr):
    length = len(arr)
    if length == 2:
        return find_distance(arr[0], arr[1]), arr[0], arr[1]
    if length == 1:
        return float("inf"), arr[0]
    left = find_most_closest_points(arr[:length // 2])
    right = find_most_closest_points(arr[length // 2:])
    delta = min(left[0], right[0]) / 2
    median = arr[length // 2]
    median_arr = [i for i in arr if median[0] - delta < i[0] < median[0] + delta and i != median]
    median = find_distance_point_arr(median, median_arr)
    return min([left, median, right], key=lambda x: x[0])


def main_fun_of_find_distance(arr):
    arr.sort(key=lambda x: x[0])
    return find_most_closest_points(arr)


def main():
    arr = [(randint(-10000, 10000), randint(-10000, 10000)) for i in range(10 ** 4)]
    result = main_fun_of_find_distance(arr)
    print(f"min distance is {result[0]} the most closest points are {result[1:]}")

    
if __name__ == "__main__":
    main()
 ```
