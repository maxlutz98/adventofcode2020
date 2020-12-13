import math

from typing import List, Tuple, Dict


def read_input(filename: str) -> Tuple[int, List[int]]:
    data = []
    for line in open(filename, "r"):
        data.append(line)
    estimate = int(data[0])
    buses = sorted([int(element) for element in data[1].split(",") if element != "x"])
    return estimate, buses


def get_next_departures(estimate: int, buses: List[int]) -> Dict[int, int]:
    departures = {}
    for bus in buses:
        buffer = math.ceil(estimate / bus)
        departures[bus] = buffer * bus
    return departures


def next_bus_id(departures: Dict[int, int]) -> Tuple[int, int]:
    next_departure = min(departures.values())
    for id, time in departures.items():
        if time == next_departure:
            return id, next_departure


def main():
    estimate, buses = read_input("days/day13/input_day13.txt")
    departures = get_next_departures(estimate, buses)

    bus_id, depart = next_bus_id(departures)

    print(bus_id * (depart - estimate))

