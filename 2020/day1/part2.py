
def read_input(filename):
    f = open(filename, "r")
    data = f.readlines()
    f.close()
    return data


def find_summands(data):
    for element1 in data:
        for element2 in data:
            for element3 in data:
                if int(element1) + int(element2) + int(element3) == 2020:
                    return (element1, element2, element3)


def main():
    puzzle = read_input("days/day1/input_day1.txt")
    summands = find_summands(puzzle)
    print(summands)
    result = int(summands[0]) * int(summands[1]) * int(summands[2])
    print(result)

