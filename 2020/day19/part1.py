import re

from typing import List, Tuple, Dict


def read_input(filename: str) -> Tuple[Dict[int, str], List[str]]:
    f = open(filename, "r")
    data = f.read()
    f.close()
    rules, messages = data.split("\n\n")
    rules = rules.split("\n")
    messages = messages.split("\n")
    buffer = {}
    for rule in rules:
        splitted = rule.split(": ")
        buffer[int(splitted[0])] = splitted[1]
    rules = buffer
    return rules, messages


def resolve_rule(rules: Dict[int, str], number: int) -> str:
    value = ""
    if rules[number] == "\"a\"":
        value = "a"
    elif rules[number] == "\"b\"":
        value = "b"
    elif " | " in rules[number]:
        value += "("
        for index, part in enumerate(rules[number].split(" | ")):
            for rule in part.split(" "):
                value += resolve_rule(rules, int(rule))
            if index < len(rules[number].split(" | ")) - 1:
                value += "|"
        value += ")"
    else:
        for rule in rules[number].split(" "):
            value += resolve_rule(rules, int(rule))
    return value


def check_matching(messages: List[str], regex: str) -> int:
    amount = 0
    for message in messages:
        if re.search(regex, message):
            amount += 1
    return amount



def main():
    rules, messages = read_input("days/day19/input_day19.txt")
    number = check_matching(messages, "^" + resolve_rule(rules, 0) + "$")
    print(number)
