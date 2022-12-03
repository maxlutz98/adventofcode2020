from typing import Dict


def read_input(filename: str) -> Dict[int, int]:
    data = []
    for line in open(filename, "r"):
        data.append(line)
    buses = {}
    for index, element in enumerate(data[1].split(",")):
        if element != "x":
            buses[int(element)] = index
    return buses


def check_delays(delays: Dict[int, int]):
    multiplier = 3448275862068
    testing = True
    while testing:
        buffer = multiplier * list(delays)[0]
        number_buses = 0
        for id, delay in delays.items():
            if not (buffer + delay) % id:
                number_buses += 1
                if number_buses == len(delays):
                    return buffer
            else:
                multiplier += 1
                break


def main():
    buses = read_input("days/day13/input_day13.txt")
    print(buses)
    timestamp = check_delays(buses)
    print(timestamp)
