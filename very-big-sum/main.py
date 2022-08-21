from typing import List


def parse_input(filepath: str) -> List[int]:
    with open(filepath, 'r') as input_file:
        lines = input_file.readlines()
        if (len(lines) == 2):
            # long_ints = list(map(int, lines[1].split(' ')))
            long_ints = [int(x) for x in lines[1].rstrip().split(' ')]
            return long_ints


def a_very_big_sum(numbers: List[int]) -> int:
    return sum(numbers)


if __name__ == '__main__':
    long_ints = parse_input('./input.txt')
    long_sum = a_very_big_sum(long_ints)
    print(long_sum)
