from typing import List


def read_input(filename: str) -> List[int]:
    data = []
    for line in open(filename, "r"):
        data = [int(x) for x in line.replace("\n", "").split(",")]
    return data


def occurrences(data: List[int], searched: int) -> List[int]:
    return [index for index, value in enumerate(data) if value == searched]


def new_value(data: List[int]) -> List[int]:
    indizes = occurrences(data, data[-1])
    if len(indizes) >= 2:
        value = indizes[-1] - indizes[-2]
    elif len(indizes) == 1:
        value = 0
    else:
        print("Problem")
    return value


def iterate_multiple_times(data: List[int], amount: int) -> List[int]:
    for i in range(len(data), amount):
        value = new_value(data)
        data.append(value)
    return data


def main():
    data = read_input("days/day15/input_day15.txt")
    game = iterate_multiple_times(data, 2020)
    print(game[-1])
