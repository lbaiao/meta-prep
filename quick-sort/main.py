# https://www.hackerrank.com/challenges/quicksort1/problem?isFullScreen=true
# https://www.hackerrank.com/challenges/quicksort2/problem

def print_arr(arr):
    print(''.join(str(i) + ' ' for i in arr))


def quick_sort(arr):
    if (len(arr) < 1):
        return arr
    
    left = []
    right = []
    equal = []
    for i in arr:
        if (i < arr[0]):
            left.append(i)
        elif (i > arr[0]):
            right.append(i)
        else:
            equal.append(i)
            
    if (len(left) > 1):
        left = quick_sort(left)
    if (len(right) > 1):        
        right = quick_sort(right)
    
    arr = [*left, *equal, *right]
    print_arr(arr)

    return arr


if __name__ == '__main__':
    arr = [3, 1, 2, 4]
    print(quick_sort(arr))

