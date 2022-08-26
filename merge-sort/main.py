from typing import List
import random

def merge_sort(array: List[int]) -> List[int]:
    if len(array) == 1:
        return array

    middle = int(len(array) / 2)
    arr1 = array[:middle]
    arr2 = array[middle:]

    arr1 = merge_sort(arr1)
    arr2 = merge_sort(arr2)

    return merge(arr1, arr2)


def merge(arr1, arr2) -> List[int]:
    result = []
    while len(arr1) > 0 and len(arr2) > 0:
        if arr1[0] > arr2[0]:
            result.append(arr2.pop(0))
        else:
            result.append(arr1.pop(0))

    result += arr1
    result += arr2
    return result


if __name__ == '__main__':
    # x = [1, 3, 4, 2, 1, 7, 3, 9, 0, 1]
    n_its = int(1e3)
    max_len = int(1e4)

    results = []
    print_its = n_its - 1
    for i in range(n_its):
        rnd_len = random.randrange(1, max_len)
        arr = [random.randrange(0, rnd_len) for _ in range(rnd_len)]
        res = merge_sort(arr) == sorted(arr)
        results.append(1 if merge_sort(arr) else 0)
        print(f'{i}/{print_its}')

    acc = sum(results) / len(results)
    print(acc * 100)

