import re
from typing import List, Tuple, Dict


def read_input(filename: str) -> Tuple[List[str], List[str], List[str]]:
    f = open(filename, "r")
    data = f.read()
    f.close()
    rules, yours, others = data.split("\n\n")
    return rules, yours, others


def process_rules(raw: List[str]) -> Dict[str, List[int]]:
    rules = {}
    raw = raw.split("\n")
    for line in raw:
        key = line.split(": ")[0]
        values = [int(x) for x in re.findall("\d+", line)]
        rules[key] = values
    return rules


def process_tickets(raw: List[str]) -> List[List[int]]:
    raw = raw.split("\n")
    raw.pop(0)
    tickets = []
    for line in raw:
        values = [int(x) for x in line.split(",")]
        tickets.append(values)
    return tickets


def check_validity(ticket: List[int], rules: Dict[str, List[int]]) -> List[int]:
    valid_values = []
    for value in ticket:
        valid = False
        for key, borders in rules.items():
            if borders[0] <= value <= borders[1] or borders[2] <= value <= borders[3]:
                valid = True
        if valid is False:
            valid_values.append(value)
    return valid_values


def check_tickets(tickets: List[List[int]], rules: Dict[str, List[int]]) -> int:
    error_rate = 0
    for ticket in tickets:
        error_rate += sum(check_validity(ticket, rules))
    return error_rate


def main():
    data = read_input("days/day16/input_day16.txt")
    tickets = process_tickets(data[2])
    rules = process_rules(data[0])
    error = check_tickets(tickets, rules)
    print(error)
