import math


def read_input(filename):
    f = open(filename, "r")
    data = f.readlines()
    f.close()
    return data


def process_input(puzzle: list()):
    data = list()
    for element in puzzle:
        row = get_row(element[:7])
        column = get_column(element[7:])
        id = calculate_seat_id(row, column)
        data.append(id)
    return data



def get_row(code):
    border = (0, 127)
    for i in range(0, 7):
        if code[i] == "F":
            border = (border[0], math.floor((border[0] + border[1]) / 2))
        else:
            border = (math.ceil((border[0] + border[1]) / 2), border[1])

    return border[0]


def get_column(code):
    border = (0, 7)
    for i in range(0, 3):
        if code[i] == "L":
            border = (border[0], math.floor((border[0] + border[1]) / 2))
        else:
            border = (math.ceil((border[0] + border[1]) / 2), border[1])

    return border[0]


def calculate_seat_id(row, column):
    return row * 8 + column

def get_maximum(data):
    result = data[0]
    for element in data:
        if result < element:
            result = element
    return result


def get_minimum(data):
    result = data[0]
    for element in data:
        if result > element:
            result = element
    return result


def find_missing_seat(seat_ids, borders):
    for i in range(borders[0], borders[1] + 1):
        if i not in seat_ids:
            return i


def main():
    puzzle = read_input("days/day5/input_day5.txt")
    data = process_input(puzzle)
    highest_id = get_maximum(data)
    smallest_id = get_minimum(data)
    seat_id = find_missing_seat(data, (smallest_id, highest_id))
    print(seat_id)

