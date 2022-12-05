import re
from typing import List


def read_input(filename):
    f = open(filename, "r")
    data = f.read().splitlines()
    f.close()
    return data


def create_stacks(stack_text: List[str]) -> List[List[int]]:
    stacks = [[], [], [], [], [], [], [], [], [], []]
    for i in range(1, 10):
        stack = []
        for x in range(1, 9):
            if stack_text[x - 1][1 + (i - 1) * 4] != " ":
                stack.append(stack_text[x - 1][1 + (i - 1) * 4])
        stacks[i] = stack
    return stacks


def part1(puzzle: List[str], stacks: List[List[int]]) -> str:
    result = ""
    for line in puzzle:
        matches = re.findall(r"\d+", line)
        amount, source, target = map(int, matches)
        for i in range(amount):
            stacks[target].insert(0, stacks[source].pop(0))
    for i in range(1, 10):
        result += stacks[i][0]
    return result


def part2(puzzle: List[str], stacks: List[List[int]]) -> str:
    result = ""
    for line in puzzle:
        buffer = ""
        matches = re.findall(r"\d+", line)
        amount, source, target = map(int, matches)
        for i in range(amount):
            buffer += stacks[source].pop(0)
        for crate in buffer[::-1]:
            stacks[target].insert(0, crate)
    for i in range(1, 10):
        result += stacks[i][0]
    return result


def main():
    puzzle = read_input("input.txt")
    stacks = create_stacks(puzzle[0:9])
    print(part1(puzzle[10:], stacks))
    stacks = create_stacks(puzzle[0:9])
    print(part2(puzzle[10:], stacks))


if __name__ == "__main__":
    main()
