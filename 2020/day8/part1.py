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
    return acc


def main():
    puzzle = read_input("days/day8/input_day8.txt")
    data = process_input(puzzle)
    acc = execute_commands(data)
    print(acc)
