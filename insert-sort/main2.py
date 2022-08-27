def insertion_sort1(n, arr):
    in_element = arr[n-1]
    for i in list(range(n-1))[::-1]:
        if in_element <= arr[i]:
            arr[i+1] = arr[i]
        else:
            arr[i+1] = in_element
            break
    if (in_element <= arr[0]):
        arr[0] = in_element
    return arr


def print_output(arr):
    print(''.join([str(a) + ' ' for a in arr]))


def insertion_sort2(n, arr):
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            arr[:i+1] = insertion_sort1(i+1, arr[:i+1])
        print_output(arr)


if __name__ == '__main__':
    arr1 = [3, 4, 7, 5, 6, 2, 1]
    arr2 = [1, 4, 3, 5, 6, 2]

    # insertion_sort2(7, arr1)
    insertion_sort2(6, arr2)


