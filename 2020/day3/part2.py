def read_input(filename):
    f = open(filename, "r")
    data = f.readlines()
    f.close()
    return data


def calculate_trajectory(puzzle, steps, vertical=1):
    trees = 0
    first = 0
    for index, line in enumerate(puzzle):
        if not index % vertical:
            if first:
                position += steps
            else:
                position = 0
                first = 1
            if position > 30:
                position = position % 31
            if line[position] == "#":
                trees += 1
    return trees


def main():
    puzzle = read_input("days/day3/input_day3.txt")
    steps = 3
    trees = (calculate_trajectory(puzzle, 1), calculate_trajectory(puzzle, 3), calculate_trajectory(puzzle, 5),
             calculate_trajectory(puzzle, 7), calculate_trajectory(puzzle, 1, vertical=2))
    result = 1
    for element in trees:
        result = result * int(element)

    print(result)
