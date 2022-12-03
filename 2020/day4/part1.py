def read_input(filename):
    f = open(filename, "r")
    data = f.read()
    f.close()
    return data


def check_passports(data):
    valid = 0
    for element in data:
        if "byr" in element and "iyr" in element and "eyr" in element and "hgt" in element and "hcl" in element and "ecl" in element and "pid" in element:
            valid += 1
    return valid


def main():
    puzzle = read_input("days/day4/input_day4.txt")
    puzzle = puzzle.split("\n\n")

    valid = check_passports(puzzle)
    print(valid)
