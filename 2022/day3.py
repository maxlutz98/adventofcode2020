from typing import List


def read_input(filename):
    f = open(filename, "r")
    data = f.read().splitlines()
    f.close()
    return data


def char_value(character: str) -> int:
    if character.isupper():
        value = ord(character) - 38
    else:
        value = ord(character) - 96
    return value


def part1(puzzle: List[str]) -> None:
    result = 0
    for line in puzzle:
        firstpart, secondpart = list(line[: len(line) // 2]), list(
            line[len(line) // 2 :]
        )
        result += char_value(list(set(firstpart).intersection(secondpart))[0])
    print(result)


def part2(puzzle: List[str]) -> None:
    result = 0
    for x in range(len(puzzle) // 3):
        first, second, third = puzzle[x * 3 : (x + 1) * 3]
        result += char_value(list(set(first).intersection(second, third))[0])
    print(result)


def main():
    puzzle = read_input("input.txt")
    part1(puzzle)
    part2(puzzle)


if __name__ == "__main__":
    main()
