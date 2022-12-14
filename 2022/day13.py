from functools import cmp_to_key
from typing import List


def read_input(filename):
    f = open(filename, "r")
    data = f.read().split("\n\n")
    f.close()
    return data


def compare_lists_order(left, right) -> bool:
    order = None
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            order = True
        elif left == right:
            pass
        elif left > right:
            order = False
    elif isinstance(left, list) and isinstance(right, list):
        for index in range(min(len(left), len(right))):
            order = compare_lists_order(left[index], right[index])
            if order != None:
                break
        if order == None:
            if len(left) < len(right):
                order = True
            elif len(left) > len(right):
                order = False
    elif isinstance(left, list) and isinstance(right, int):
        order = compare_lists_order(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
        order = compare_lists_order([left], right)
    return order


def compare_wrapper(left, right) -> int:
    if compare_lists_order(left, right):
        return 1
    elif not compare_lists_order(left, right):
        return -1
    return 0


def part1(puzzle: List[str]) -> int:
    result = 0
    left, right = list(), list()
    for pair_index, pair in enumerate(puzzle, start=1):
        left, right = eval(pair.split()[0]), eval(pair.split()[1])
        if compare_lists_order(left, right) == True:
            result += pair_index
    return result


def part2(puzzle: List[str]) -> int:
    left, right = list(), list()
    divider_packets = [[[2]], [[6]]]
    lists = [] + divider_packets
    for pair in puzzle:
        left, right = eval(pair.split()[0]), eval(pair.split()[1])
        lists.append(left)
        lists.append(right)
    lists = sorted(lists, key=cmp_to_key(compare_wrapper), reverse=True)
    return (lists.index(divider_packets[0]) + 1) * (lists.index(divider_packets[1]) + 1)


def part3(puzzle: List[str]) -> int:
    left, right = list(), list()
    divider_packets = [[[2]], [[6]]]
    lists = [] + divider_packets
    for pair in puzzle:
        left, right = eval(pair.split()[0]), eval(pair.split()[1])
        lists.append(left)
        lists.append(right)
    lists = sorted(lists, key=cmp_to_key(compare_wrapper), reverse=True)
    for index_1 in reversed(range(len(lists))):
        for index_2 in range(index_1):
            if not compare_lists_order(lists[index_2], lists[index_2 + 1]):
                buffer = lists[index_2].copy()
                lists[index_2] = lists[index_2 + 1].copy()
                lists[index_2 + 1] = buffer.copy()
    return (lists.index(divider_packets[0]) + 1) * (lists.index(divider_packets[1]) + 1)


def main():
    puzzle = read_input("input.txt")
    print(part1(puzzle))
    print(part2(puzzle))
    print(part3(puzzle))


if __name__ == "__main__":
    main()
