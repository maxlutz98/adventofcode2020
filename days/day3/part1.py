
def read_input(filename):
    f = open(filename, "r")
    data = f.readlines()
    f.close()
    return data


def calculate_trajectory(puzzle, position):
    trees = 0
    position -= 3
    for line in puzzle:
        position += 3
        if position > 30:
            position = position % 31
        if line[position] == "#":
            trees += 1
        print(line[position])
        print(position)
    return trees



def main():
    puzzle = read_input("days/day3/input_day3.txt")
    position = 0
    trees = calculate_trajectory(puzzle, position)
    print(trees)


