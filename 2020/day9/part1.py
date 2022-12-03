def read_input(filename):
    f = open(filename, "r")
    data = f.readlines()
    f.close()
    return data


def get_false_number(puzzle: list()):
    preamble = 25
    first = preamble
    for index in range(preamble, len(puzzle)):
        valid = False
        for index1 in range(0, preamble):
            for index2 in range(0, preamble):
                if index2 != index1:
                    if int(puzzle[index - (index1 + 1)]) + int(puzzle[index - (index2 + 1)]) == int(puzzle[index]):
                        valid = True
        if not valid:
            number = puzzle[index]
            return number


def main():
    puzzle = read_input("days/day9/input_day9.txt")
    result = get_false_number(puzzle)
    print(result)
