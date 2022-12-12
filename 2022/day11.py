from __future__ import annotations

from typing import List, Tuple


class Monkey:
    def __init__(
        self, items: List[int], operation: str, test: Tuple[(int,) * 3], part="part1"
    ) -> None:
        self.items = items
        self.operation = operation
        self.test = test
        self.activity = 0
        self.part = part

    def receive_item(self, item: int):
        self.items.append(item)

    def inspect_item(self) -> None:
        old = self.items[0]
        new = 0
        new = eval(self.operation)
        if self.part == "part1":
            new = new // 3
        else:
            new = new % (2 * 3 * 5 * 7 * 11 * 13 * 17 * 19)
        self.items[0] = new
        self.activity += 1

    def test_item(self, monkeys: List[(Monkey,) * 8]) -> None:
        if not self.items[0] % self.test[0]:
            receiver = self.test[1]
        else:
            receiver = self.test[2]
        monkeys[receiver].receive_item(self.items.pop(0))

    def execute_turn(self, monkeys: List[(Monkey,) * 8]) -> None:
        for item in range(len(self.items)):
            self.inspect_item()
            self.test_item(monkeys)


def part1() -> int:
    example = 0
    if example:
        monkeys = [
            Monkey([79, 98], "old * 19", (23, 2, 3)),
            Monkey([54, 65, 75, 74], "old + 6", (19, 2, 0)),
            Monkey([79, 60, 97], "old * old", (13, 1, 3)),
            Monkey([74], "old + 3", (17, 0, 1)),
        ]
    else:
        monkeys = [
            Monkey([56, 52, 58, 96, 70, 75, 72], "old * 17", (11, 2, 3)),
            Monkey([75, 58, 86, 80, 55, 81], "old + 7", (3, 6, 5)),
            Monkey([73, 68, 73, 90], "old * old", (5, 1, 7)),
            Monkey([72, 89, 55, 51, 59], "old + 1", (7, 2, 7)),
            Monkey([76, 76, 91], "old * 3", (19, 0, 3)),
            Monkey([88], "old + 4", (2, 6, 4)),
            Monkey([64, 63, 56, 50, 77, 55, 55, 86], "old + 8", (13, 4, 0)),
            Monkey([79, 58], "old + 6", (17, 1, 5)),
        ]
    rounds = 20
    activities = []
    for i in range(rounds):
        for monkey in monkeys:
            monkey.execute_turn(monkeys)
    for monkey in monkeys:
        activities.append(monkey.activity)
    activities = sorted(activities, reverse=True)
    return activities[0] * activities[1]


def part2() -> int:
    monkeys = [
        Monkey([56, 52, 58, 96, 70, 75, 72], "old * 17", (11, 2, 3), part="part2"),
        Monkey([75, 58, 86, 80, 55, 81], "old + 7", (3, 6, 5), part="part2"),
        Monkey([73, 68, 73, 90], "old * old", (5, 1, 7), part="part2"),
        Monkey([72, 89, 55, 51, 59], "old + 1", (7, 2, 7), part="part2"),
        Monkey([76, 76, 91], "old * 3", (19, 0, 3), part="part2"),
        Monkey([88], "old + 4", (2, 6, 4), part="part2"),
        Monkey([64, 63, 56, 50, 77, 55, 55, 86], "old + 8", (13, 4, 0), part="part2"),
        Monkey([79, 58], "old + 6", (17, 1, 5), part="part2"),
    ]
    rounds = 10000
    activities = []
    for i in range(rounds):
        for monkey in monkeys:
            monkey.execute_turn(monkeys)
    for monkey in monkeys:
        activities.append(monkey.activity)
    activities = sorted(activities, reverse=True)
    return activities[0] * activities[1]


def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()
