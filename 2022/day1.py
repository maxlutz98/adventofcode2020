
def read_input(filename):
    f = open(filename, "r")
    data = f.read()
    f.close()
    return data


def main():
    puzzle = read_input("input.txt")
    calories = list()
    elves = puzzle.split("\n\n")
    for elf in elves:
        calories.append(sum([int(number) for number in elf.split("\n")]))
    print(max(calories))
    calories = sorted(calories, reverse=True)
    print(sum(calories[0:3]))


if __name__ == '__main__':
    main()


