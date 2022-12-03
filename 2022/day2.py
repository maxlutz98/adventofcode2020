values = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}


def read_input(filename):
    f = open(filename, "r")
    data = f.read().splitlines()
    f.close()
    return data


def part1():
    games = read_input("input.txt")
    points = 0
    for round in games:
        points += values[round[-1]]
        if (
            values[round[-1]] - values[round[0]] == 1
            or values[round[-1]] - values[round[0]] == -2
        ):
            points += 6
        elif values[round[-1]] == values[round[0]]:
            points += 3
        else:
            pass
    print(points)


def part2():
    games = read_input("input.txt")
    points = 0
    for round in games:
        if values[round[-1]] == values["X"]:
            points += values[round[0]] - 1 if values[round[0]] - 1 > 0 else values["C"]
        elif values[round[-1]] == values["Y"]:
            points += 3
            points += values[round[0]]
        elif values[round[-1]] == values["Z"]:
            points += values[round[0]] + 1 if values[round[0]] + 1 <= 3 else values["A"]
            points += 6
        else:
            pass
    print(points)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
