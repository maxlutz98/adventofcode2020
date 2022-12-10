from typing import List

import numpy as np


def read_input(filename):
    f = open(filename, "r")
    data = f.read().splitlines()
    f.close()
    return data


def part1(puzzle: List[str]) -> int:
    head = np.array([0, 0])
    tail = np.array([0, 0])
    positions = [[0, 0]]
    for line in puzzle:
        direction, amount = line.split(" ")
        amount = int(amount)
        for step in range(amount):
            if direction == "U":
                head[1] += 1
            elif direction == "D":
                head[1] -= 1
            elif direction == "R":
                head[0] += 1
            elif direction == "L":
                head[0] -= 1

            distance = head - tail
            if distance[0] * distance[0] + distance[1] * distance[1] >= 4:
                distance = np.clip(distance, -1, 1)
                tail += distance
                if [tail[0], tail[1]] not in positions:
                    positions.append([tail[0], tail[1]])
    return len(positions)


def part2(puzzle: List[str]) -> int:
    knots = np.zeros((10, 2))
    positions = [[0, 0]]
    for line in puzzle:
        direction, amount = line.split(" ")
        amount = int(amount)
        for step in range(amount):
            if direction == "U":
                knots[0][1] += 1
            elif direction == "D":
                knots[0][1] -= 1
            elif direction == "R":
                knots[0][0] += 1
            elif direction == "L":
                knots[0][0] -= 1
            
            for index, knot in enumerate(knots):
                if index != 0:
                    distance = knots[index - 1] - knot
                    if distance[0] * distance[0] + distance[1] * distance[1] >= 4:
                        distance = np.clip(distance, -1, 1)
                        knot += distance
                        if index == 9:
                            if [knot[0], knot[1]] not in positions:
                                positions.append([knot[0], knot[1]])
                else:
                    pass
    return len(positions)

def main():
    puzzle = read_input("input.txt")
    print(part1(puzzle))
    print(part2(puzzle))


if __name__ == "__main__":
    main()
