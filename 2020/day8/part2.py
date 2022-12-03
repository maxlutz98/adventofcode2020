import copy


def read_input(filename):
    f = open(filename, "r")
    data = f.readlines()
    f.close()
    return data


def process_input(puzzle: list()):
    data = list()
    for index in range(0, len(puzzle)):
        splitted = puzzle[index].replace("\n", "").split(" ")
        data.append([splitted[0], splitted[1], 0])
    return data


def execute_commands(commands):
    counter = 0
    acc = 0
    failed = False
    while counter < len(commands) and commands[counter][2] < 1:
        commands[counter][2] += 1
        if commands[counter][0] == "nop":
            counter += 1
        elif commands[counter][0] == "jmp":
            counter += int(commands[counter][1])
        elif commands[counter][0] == "acc":
            acc += int(commands[counter][1])
            counter += 1
        else:
            print(commands[counter][0])

    if counter < len(commands):
        failed = True

    return acc, failed


def main():
    puzzle = read_input("days/day8/input_day8.txt")
    data = process_input(puzzle)
    acc = None
    for index in range(0, len(data)):
        data2 = copy.deepcopy(data)
        failed = True
        if data[index][0] == "jmp":
            data2[index] = ["nop", data[index][1], data[index][2]]
            acc, failed = execute_commands(data2)
        elif data[index][0] == "nop":
            data2[index] = ["jmp", data[index][1], data[index][2]]
            acc, failed = execute_commands(data2)
        else:
            pass

        if failed is False:
            print(acc)
