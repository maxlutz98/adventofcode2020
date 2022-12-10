from typing import List


def read_input(filename):
    f = open(filename, "r")
    data = f.read().splitlines()
    f.close()
    return data


def calculate_signal(cycles: int, x: int) -> int:
    buffer = 0
    if cycles == 20 or (cycles - 20) % 40 == 0:
        buffer += x * cycles
    return buffer


def generate_sprite(x: int) -> str:
    return "." * (x - 1) + "#" * 3 + "." * (39 - (x + 1))


def format_drawing(cycles: int) -> str:
    return "\n" if cycles % 40 == 0 else ""


def part1(puzzle: List[str]) -> int:
    x = 1
    cycles = 0
    signal = 0
    for line in puzzle:
        if "noop" in line:
            cycles += 1
            signal += calculate_signal(cycles, x)
        else:
            cycles += 1
            signal += calculate_signal(cycles, x)
            cycles += 1
            signal += calculate_signal(cycles, x)
            x += int(line.split(" ")[1])
    return signal


def part2(puzzle: List[str]) -> str:
    x = 1
    sprite = generate_sprite(x)
    cycles = 0
    drawing = ""
    for line in puzzle:
        if "noop" in line:
            drawing += sprite[cycles % 40]
            cycles += 1
            drawing += format_drawing(cycles)
        else:
            drawing += sprite[cycles % 40]
            cycles += 1
            drawing += format_drawing(cycles)
            drawing += sprite[cycles % 40]
            cycles += 1
            drawing += format_drawing(cycles)
            x += int(line.split(" ")[1])
            sprite = generate_sprite(x)
    return drawing


def main():
    puzzle = read_input("input.txt")
    print(part1(puzzle))
    print(part2(puzzle))


if __name__ == "__main__":
    main()
