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
    invalid_tickets = []
    for index, ticket in enumerate(tickets):
        if check_validity(ticket, rules):
            invalid_tickets.append(index)
    return invalid_tickets


def clean_tickets(tickets: List[List[int]], invalid: List[int]) -> List[List[int]]:
    invalid_rev = reversed(sorted(invalid))
    for index in invalid_rev:
        del tickets[index]
    return tickets


def identify_order(tickets: List[List[int]], rules: Dict[str, List[int]]) -> Dict[int, str]:
    suitable = {}
    for field in range(0, len(tickets[0])):
        for key, borders in rules.items():
            valid = True
            for ticket in tickets:
                if not (borders[0] <= ticket[field] <= borders[1] or borders[2] <= ticket[field] <= borders[3]):
                    valid = False
            if valid is True:
                if field in suitable:
                    suitable[field] += [key]
                else:
                    suitable[field] = [key]
    while sum([len(x) for x in suitable.values()]) != len(suitable):
        for field in range(0, len(tickets[0])):
            if len(suitable[field]) == 1:
                for index in range(0, len(suitable)):
                    if index != field:
                        if suitable[field][0] in suitable[index]:
                            suitable[index].remove(suitable[field][0])
    return suitable


def multiply_departure_fields(ticket: List[int], order: Dict[int, List[str]]) -> int:
    result = 1
    for key, value in order.items():
        if value[0].startswith("departure"):
            result *= ticket[key]
    return result


def main():
    data = read_input("days/day16/input_day16.txt")
    tickets = process_tickets(data[2])
    rules = process_rules(data[0])
    invalid = check_tickets(tickets, rules)
    tickets = clean_tickets(tickets, invalid)
    order = identify_order(tickets, rules)
    my_ticket = process_tickets(data[1])[0]
    result = multiply_departure_fields(my_ticket, order)
    print(result)
