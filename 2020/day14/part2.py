import math
import re

from typing import List, Tuple, Dict, Union


def read_input(filename: str) -> List[Union[str, Dict[int, int]]]:
    data = []
    for line in open(filename, "r"):
        data.append(line.replace("\n", ""))
    mask = None
    memory = {}
    puzzle_input = []
    for index, element in enumerate(data):
        if index == 0:
            mask = element.split(" = ")[-1]
        elif index == len(data) - 1:
            string = element.split(" = ")
            match = re.findall("\d+", string[0])
            memory[int(match.pop())] = int(string[-1])
            puzzle_input.append([mask, memory])
        elif element.startswith("mask"):
            puzzle_input.append([mask, memory])
            mask = element.split(" = ")[-1]
            memory = {}
        else:
            string = element.split(" = ")
            match = re.findall("\d+", string[0])
            memory[int(match.pop())] = int(string[-1])
    return puzzle_input


def number_to_binary(number: int) -> str:
    return "{:036b}".format(number)


def binary_to_number(string: str) -> int:
    return int(string, 2)


def apply_mask(mask: str, number_bin: str) -> str:
    for index, character in enumerate(mask):
        if character == "1":
            number_bin = number_bin[:index] + "1" + number_bin[index + 1:]
        elif character == "0":
            number_bin = number_bin[:index] + "0" + number_bin[index + 1:]
        else:
            pass
    return number_bin


def process_data(data: List[Union[str, Dict[int, int]]]) -> Dict[int, int]:
    memory = {}
    for set in data:
        for key, value in set[1].items():
            memory[key] = binary_to_number(apply_mask(set[0], number_to_binary(value)))
    return memory


def main():
    buffer = read_input("days/day14/input_day14.txt")
    print(buffer)
    memory = process_data(buffer)
    print(memory)
    print(sum(memory.values()))

