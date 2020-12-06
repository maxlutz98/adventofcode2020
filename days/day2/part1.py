import re


def read_input(filename):
    f = open(filename, "r")
    data = f.readlines()
    f.close()
    return data


def process_input(puzzle: list()):
    data = list()
    for line in puzzle:
        regex = re.findall("\d+", line)
        minimal = int(regex[0])
        maximal = int(regex[1])
        character = re.findall("(\S):", line)[0]
        password = re.findall(":\s(\S*)", line)[0]
        data.append((minimal, maximal, character, password))

    return data


def validate_passwords(data):
    valid = 0
    for element in data:
        if element[0] <= element[3].count(element[2]) <= element[1]:
            valid += 1

    return valid


def main():
    puzzle = read_input("days/day2/input_day2.txt")
    data = process_input(puzzle)
    number = validate_passwords(data)
    print(number)
