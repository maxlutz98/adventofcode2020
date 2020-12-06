import re


def read_input(filename):
    f = open(filename, "r")
    data = f.read()
    f.close()
    return data


def check_passports(data):
    valid = 0
    for element in data:
        byr_buffer = re.search("byr:(\d{4})(\s|$)", element)
        iyr_buffer = re.search("iyr:(\d{4})(\s|$)", element)
        eyr_buffer = re.search("eyr:(\d{4})(\s|$)", element)
        hgt_in_buffer = re.search("hgt:(\d{2})in(\s|$)", element)
        hgt_cm_buffer = re.search("hgt:(\d{3})cm(\s|$)", element)
        hcl_buffer = re.search("hcl:#[0-9a-f]{6}(\s|$)", element)
        ecl_buffer = re.search("ecl:(amb|blu|brn|gry|grn|hzl|oth)(\s|$)", element)
        pid_buffer = re.search("pid:\d{9}(\s|$)", element)
        if byr_buffer and 1920 <= int(byr_buffer.group(1)) <= 2002 and iyr_buffer and 2010 <= int(
                iyr_buffer.group(1)) <= 2020 and eyr_buffer and 2020 <= int(eyr_buffer.group(1)) <= 2030 and (
                (hgt_cm_buffer and 150 <= int(hgt_cm_buffer.group(1)) <= 193) or (
                hgt_in_buffer and 59 <= int(hgt_in_buffer.group(1)) <= 76)) and hcl_buffer and pid_buffer and ecl_buffer:
            valid += 1
    return valid


def main():
    puzzle = read_input("days/day4/input_day4.txt")
    puzzle = puzzle.split("\n\n")

    valid = check_passports(puzzle)
    print(valid)
