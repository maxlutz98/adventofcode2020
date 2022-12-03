def read_input(filename):
    f = open(filename, "r")
    data = f.readlines()
    f.close()
    for index in range(0, len(data)):
        data[index] = int(data[index])
    return data


def put_adapters_together(puzzle):
    current_jolt = 0
    one = 0
    three = 0
    for i in range(0, len(puzzle)):
        for j in range(1, 4):
            if current_jolt + j in puzzle:
                if j == 1:
                    one += 1
                elif j == 3:
                    three += 1
                current_jolt += j
                break
    return (current_jolt + 3, one, three + 1)



def main():
    puzzle = read_input("days/day10/input_day10.txt")
    jolts = put_adapters_together(puzzle)
    print(jolts[1] * jolts[2])


