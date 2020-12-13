import math

from typing import List, Tuple


def read_input(filename: str) -> List[Tuple[str, int]]:
    data = []
    for line in open(filename, "r"):
        data.append((line[0], int(line[1:])))
    return data


def execute_instructions(instructions: List[Tuple[str, int]], position: Tuple[int], waypoint: Tuple[int]) -> Tuple[int]:
    for instruction in instructions:
        position, waypoint = process_instruction(instruction, position, waypoint)
        print(position, waypoint)
    return position


def process_instruction(instruction: Tuple[str, int], position: Tuple[int], waypoint: Tuple[int]) -> Tuple[
    Tuple[int], Tuple[int]]:
    if instruction[0] == "N":
        waypoint = (waypoint[0], waypoint[1] + instruction[1])
    elif instruction[0] == "S":
        waypoint = (waypoint[0], waypoint[1] - instruction[1])
    elif instruction[0] == "E":
        waypoint = (waypoint[0] + instruction[1], waypoint[1])
    elif instruction[0] == "W":
        waypoint = (waypoint[0] - instruction[1], waypoint[1])
    elif instruction[0] == "L":
        waypoint = waypoint[0] * round(math.cos(math.radians(instruction[1]))) - round(
            math.sin(math.radians(instruction[1]))) * waypoint[1], waypoint[0] * round(
            math.sin(math.radians(instruction[1]))) + waypoint[1] * round(math.cos(math.radians(instruction[1])))
    elif instruction[0] == "R":
        waypoint = waypoint[0] * round(math.cos(math.radians(-instruction[1]))) - round(
            math.sin(math.radians(-instruction[1]))) * waypoint[1], waypoint[0] * round(
            math.sin(math.radians(-instruction[1]))) + waypoint[1] * round(math.cos(math.radians(-instruction[1])))
    elif instruction[0] == "F":
        position = (position[0] + waypoint[0] * instruction[1],
                    position[1] + waypoint[1] * instruction[1])
    else:
        print("False instruction")
    return position, waypoint


def calculate_manhatten_distance(position: Tuple[int]) -> int:
    return abs(position[0]) + abs(position[1])


def main():
    position = (0, 0)
    waypoint = (10, 1)

    nav_instructions = read_input("days/day12/input_day12.txt")
    print(nav_instructions)
    position = execute_instructions(nav_instructions, position, waypoint)
    result = calculate_manhatten_distance(position)
    print(result)
