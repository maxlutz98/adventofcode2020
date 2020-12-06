
def read_input(filename):
    f = open(filename, "r")
    data = f.readlines()
    f.close()
    return data


def find_summands(data):
    for element1 in data:
        for element2 in data:
            if int(element1) + int(element2) == 2020:
                return (element1, element2)


def main():
    puzzle = read_input("days/day1/input_day1.txt")
    summands = find_summands(puzzle)
    result = int(summands[0]) * int(summands[1])
    print(result)

