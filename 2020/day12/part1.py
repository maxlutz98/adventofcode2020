import math

from typing import List, Tuple


def read_input(filename: str) -> List[Tuple[str, int]]:
    data = []
    for line in open(filename, "r"):
        data.append((line[0], int(line[1:])))
    return data


def execute_instructions(instructions: List[Tuple[str, int]], position: Tuple[int], heading: int) -> Tuple[int]:
    for instruction in instructions:
        position, heading = process_instruction(instruction, position, heading)
        print(position, heading)
    return position


def process_instruction(instruction: Tuple[str, int], position: Tuple[int], heading: int) -> Tuple[Tuple[int], int]:
    if instruction[0] == "N":
        position = (position[0], position[1] + instruction[1])
    elif instruction[0] == "S":
        position = (position[0], position[1] - instruction[1])
    elif instruction[0] == "E":
        position = (position[0] + instruction[1], position[1])
    elif instruction[0] == "W":
        position = (position[0] - instruction[1], position[1])
    elif instruction[0] == "L":
        heading += instruction[1]
    elif instruction[0] == "R":
        heading -= instruction[1]
    elif instruction[0] == "F":
        position = (position[0] + round(math.cos(math.radians(heading)) * instruction[1]),
                    position[1] + round(math.sin(math.radians(heading)) * instruction[1]))
    else:
        print("False instruction")
    return position, heading


def calculate_manhatten_distance(position: Tuple[int]) -> int:
    return abs(position[0]) + abs(position[1])


def main():
    position = (0, 0)
    heading = 0

    nav_instructions = read_input("days/day12/input_day12.txt")
    print(nav_instructions)
    position = execute_instructions(nav_instructions, position, heading)
    result = calculate_manhatten_distance(position)
    print(result)
