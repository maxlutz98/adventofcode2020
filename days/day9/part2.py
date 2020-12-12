from typing import Dict, Iterable, List

def read_input(filename):
    f = open(filename, "r")
    data = f.readlines()
    f.close()
    for i in range(0, len(data)):
        data[i] = int(data[i])
    return data


def get_false_number(puzzle: list()):
    preamble = 25
    first = preamble
    for index in range(preamble, len(puzzle)):
        valid = False
        for index1 in range(0, preamble):
            for index2 in range(0, preamble):
                if index2 != index1:
                    if puzzle[index - (index1 + 1)] + puzzle[index - (index2 + 1)] == puzzle[index]:
                        valid = True
        if not valid:
            number = puzzle[index]
            return number


def get_contiguous_set(puzzle: list(), number: int):
    index = puzzle.index(number)
    for index1 in range(0, len(puzzle)):
        used = [puzzle[index1]]
        for index2 in range(index1 + 1, len(puzzle)):
            used.append(puzzle[index2])
            if sum(used) > int(number):
                print("too big")
                break
            elif sum(used) == number:
                return used


def first_group_with_sum(target_sum: int,
                         numbers: List[int]) -> Iterable[int]:
    for group_size in range(2, len(numbers)):
        for group in zip(*(numbers[i:] for i in range(group_size))):
            if sum(group) == target_sum:
                return group


def main():
    puzzle = read_input("days/day9/input_day9.txt")
    number = get_false_number(puzzle)
    result = get_contiguous_set(puzzle, number)
    print(min(result) + max(result))