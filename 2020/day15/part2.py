from typing import List, Dict, Tuple


def read_input(filename: str) -> Tuple[Dict[int, List[int]], int]:
    data = []
    for line in open(filename, "r"):
        data = [int(x) for x in line.replace("\n", "").split(",")]
    last_value = data[-1]
    numbers = {}
    for index, value in enumerate(data):
        numbers[value] = [index]
    return numbers, last_value


def new_value(data: Dict[int, List[int]], last: int) -> int:
    index = max(data[last]) + 1
    if len(data[last]) >= 2:
        value = max(data[last]) - min(data[last])
    elif len(data[last]) == 1:
        value = 0
    else:
        print("Problem")
    if value in data:
        if len(data[value]) == 2:
            data[value].remove(min(data[value]))
        data[value].append(index)
    else:
        data[value] = [index]

    return data, value


def iterate_multiple_times(data: Dict[int, List[int]], last: int, amount: int) -> Tuple[Dict[int, List[int]], int]:
    for i in range(len(data), amount):
        data, last = new_value(data, last)
    return data, last


def main():
    data, last_value = read_input("days/day15/input_day15.txt")
    game, searched_value = iterate_multiple_times(data, last_value, 30000000)
    print(searched_value)
