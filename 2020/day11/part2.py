from typing import List, Tuple

def read_input(filename: str) -> List[str]:
    data = []
    for line in open(filename, "r"):
        data.append(line.replace("\n", ""))
    return data


def check_adjacent_seats(puzzle: List[str], seat: Tuple[int]) -> int:
    occupied_seats = 0
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),            (0, 1),
        (1, -1), (1, 0), (1, 1)
                  ]
    for direction in directions:
        multiplier = 1
        direction_orig = direction
        while 0 <= seat[0] + direction[0] < len(puzzle) and 0 <= seat[1] + direction[1] < len(puzzle[0]) and is_floor(puzzle[seat[0] + direction[0]][seat[1] + direction[1]]):
            multiplier += 1
            direction = tuple(x * multiplier for x in direction_orig)
        if 0 <= seat[0] + direction[0] < len(puzzle) and 0 <= seat[1] + direction[1] < len(puzzle[0]):
            if is_occupied(puzzle[seat[0] + direction[0]][seat[1] + direction[1]]):
                occupied_seats += 1
    return occupied_seats


def is_occupied(seat_symbol: str) -> bool:
    return seat_symbol == "#"


def is_empty(seat_symbol: str) -> bool:
    return seat_symbol == "L"


def is_floor(symbol: str) -> bool:
    return symbol == "."


def calculate_new_seats(layout: List[str]) -> List[str]:
    new_layout = layout.copy()
    for row, row_content in enumerate(layout):
        for column, column_content in enumerate(row_content):
            if is_occupied(column_content) and check_adjacent_seats(layout, (row, column)) >= 5:
                new_layout[row] = new_layout[row][:column] + "L" + new_layout[row][column + 1:]
            elif is_empty(column_content) and check_adjacent_seats(layout, (row, column)) == 0:
                new_layout[row] = new_layout[row][:column] + "#" + new_layout[row][column + 1:]
    return new_layout


def count_occupied_seats(layout: List[str]) -> int:
    return sum([row.count("#") for row in layout])


def main():
    seat_layout = read_input("days/day11/input_day11.txt")
    old_layout = None
    while seat_layout != old_layout:
        old_layout = seat_layout.copy()
        seat_layout = calculate_new_seats(seat_layout)
    print(count_occupied_seats(seat_layout))

