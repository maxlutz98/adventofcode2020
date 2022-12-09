from typing import List


def read_input(filename):
    f = open(filename, "r")
    data = f.read().splitlines()
    f.close()
    return data


def part1(puzzle: List[str]) -> int:
    rows, columns = len(puzzle), len(puzzle[0])
    visible_trees = (rows - 1) * 2 + (columns - 1) * 2
    for row in range(1, rows - 1):
        for column in range(1, columns - 1):
            tree = list(map(int, puzzle[row][column]))[0]
            if (
                all([tree > int(current_row[column]) for current_row in puzzle[0:row]])
                or all(
                    [
                        tree > int(current_row[column])
                        for current_row in puzzle[row + 1 : rows]
                    ]
                )
                or all([tree > int(left) for left in puzzle[row][0:column]])
                or all(
                    [tree > int(right) for right in puzzle[row][column + 1 : columns]]
                )
            ):
                visible_trees += 1

    return visible_trees


def part2(puzzle: List[str]) -> int:
    rows, columns = len(puzzle), len(puzzle[0])
    scenic_score = -1
    for row in range(1, rows - 1):
        for column in range(1, columns - 1):
            tree = list(map(int, puzzle[row][column]))[0]
            top, right, left, bottom = 0, 0, 0, 0
            for scenic_row in reversed(range(0, row)):
                top += 1
                if tree <= int(puzzle[scenic_row][column]):
                    break
                else:
                    pass
            for scenic_column in range(column + 1, columns):
                right += 1
                if tree <= int(puzzle[row][scenic_column]):
                    break
                else:
                    pass
            for scenic_row in range(row + 1, rows):
                bottom += 1
                if tree <= int(puzzle[scenic_row][column]):
                    break
                else:
                    pass
            for scenic_column in reversed(range(0, column)):
                left += 1
                if tree <= int(puzzle[row][scenic_column]):
                    break
                else:
                    pass
            if scenic_score < top * right * bottom * left:
                scenic_score = top * right * bottom * left

    return scenic_score


def main():
    puzzle = read_input("input.txt")
    print(part1(puzzle))
    print(part2(puzzle))


if __name__ == "__main__":
    main()
