from typing import Dict, Iterable, List

def read_input(filename):
    f = open(filename, "r")
    data = f.readlines()
    f.close()
    for index in range(0, len(data)):
        data[index] = int(data[index])
    return sorted(data)


def put_adapters_together(puzzle):
    current_jolt = 0
    one = 0
    three = 0
    for i in range(0, len(puzzle)):
        for j in range(1, 4):
            if current_jolt + j in puzzle:
                if j == 1:
                    one += 1
                elif j == 3:
                    three += 1
                current_jolt += j
                break
    return (current_jolt + 3, one, three + 1)


def calculate_possibilites(puzzle, start, end):
    joltages = [start] + puzzle + [end]
    possibilities = calc_neighbours(joltages, 0)
    return possibilities


def calc_neighbours(puzzle, adapter):
    value = 0
    if adapter == puzzle[-1]:
        return 1
    else:
        for i in (1, 2, 3):
            if adapter + i in puzzle:
                value += calc_neighbours(puzzle, adapter + i)
            else:
                pass
    return value


def get_neighbors(adapters: list()):
    neighbours = {}
    for adapter in adapters:
        buffer = []
        for x in (1, 2, 3):
            if adapter + x in adapters:
                buffer.append(adapter + x)
        neighbours[adapter] = buffer
    return neighbours

def calculate_paths(neighbours):
    paths = {0: 1}
    for adapter, neighbours in neighbours.items():
        for neighbour in neighbours:
            if neighbour in paths:
                paths[neighbour] += paths[adapter]
            else:
                paths[neighbour] = paths[adapter]
    return paths


def main():
    puzzle = read_input("days/day10/input_day10.txt")
    jolts = put_adapters_together(puzzle)
    # possibilities = calculate_possibilites(puzzle, 0, jolts[0])
    joltages = [0] + puzzle + [jolts[0]]
    neighbors = get_neighbors(joltages)
    num_paths = calculate_paths(neighbors)
    print(num_paths[jolts[0]])
    # print(possibilities)
