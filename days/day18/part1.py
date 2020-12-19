from typing import List


def read_input(filename: str) -> List[str]:
    data = []
    for line in open(filename, "r"):
        data.append(line.replace("\n", ""))
    return data


def calculate_term(term: str) -> int:
    if "(" in term:
        level = 0
        start = []
        end = []
        for index, character in enumerate(term):
            if character == "(":
                level += 1
                if level == 1:
                    start.append(index)
            elif character == ")":
                if level == 1:
                    end.append(index)
                level -= 1
        for index in reversed(range(0, len(start))):
            term = term[:start[index]] + str(calculate_term(term[start[index] + 1:end[index]])) + term[end[index] + 1:]
    parts = term.split(" ")
    result = int(parts.pop(0))
    for index, element in enumerate(parts):
        if element == "+":
            result += int(parts[index + 1])
        elif element == "*":
            result *= int(parts[index + 1])
    return result


def main():
    data = read_input("days/day18/input_day18.txt")
    result = 0
    for element in data:
        result += calculate_term(element)
    print(result)
