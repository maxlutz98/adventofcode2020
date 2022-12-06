from typing import List


def read_input(filename):
    f = open(filename, "r")
    data = f.read().splitlines()
    f.close()
    return data


def part1(puzzle: List[str]) -> int:
    for index, character in enumerate(puzzle):
        if len(set(puzzle[index : index + 4])) == 4:
            return index + 4


def part2(puzzle: List[str]) -> int:
    for index, character in enumerate(puzzle):
        if len(set(puzzle[index : index + 14])) == 14:
            return index + 14


def main():
    puzzle = read_input("input.txt")[0]
    print(part1(puzzle))
    print(part2(puzzle))


if __name__ == "__main__":
    main()
