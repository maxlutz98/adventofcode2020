from typing import List


def read_input(filename):
    f = open(filename, "r")
    data = f.read().splitlines()
    f.close()
    return data


def part1(puzzle: List[str]) -> None:
    result = 0
    for line in puzzle:
        first_start, first_end = map(int, line.split(",")[0].split("-"))
        second_start, second_end = map(int, line.split(",")[1].split("-"))
        if (
            first_start >= second_start
            and first_end <= second_end
            or second_start >= first_start
            and second_end <= first_end
        ):
            result += 1
    print(result)


def part2(puzzle: List[str]) -> None:
    result = 0
    for line in puzzle:
        first_start, first_end = map(int, line.split(",")[0].split("-"))
        second_start, second_end = map(int, line.split(",")[1].split("-"))
        if (
            second_end >= first_start >= second_start
            or second_end >= first_end >= second_start
            or first_end >= second_start >= first_start
            or first_end >= second_end >= first_start
        ):
            result += 1
    print(result)


def main():
    puzzle = read_input("input.txt")
    part1(puzzle)
    part2(puzzle)


if __name__ == "__main__":
    main()
