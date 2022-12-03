def read_input(filename):
    f = open(filename, "r")
    data = f.read()
    f.close()
    return data


def clean_puzzle(puzzle):
    puzzle_cleaned = list()
    for element in puzzle:
        puzzle_cleaned.append(element.replace("\n", ""))
    return puzzle_cleaned


def get_number_questions(puzzle):
    answered_questions = 0
    for element in puzzle:
        buffer = list()
        for character in element:
            buffer.append(character)
        buffer = list(dict.fromkeys(buffer))
        answered_questions += buffer.__len__()
    return answered_questions


def get_common_questions(puzzle):
    common_questions = 0
    for element in puzzle:
        splitted = element.split("\n")
        if len(splitted) == 1:
            common_questions += get_number_questions(splitted)
        else:
            for character in splitted[0]:
                truth = True
                for i, string in enumerate(splitted):
                    if character in string:
                        truth = truth and True
                    else:
                        truth = False
                if truth:
                    common_questions += 1
    return common_questions


def main():
    puzzle = read_input("days/day6/input_day6.txt")
    puzzle = puzzle.split("\n\n")

    print(get_common_questions(puzzle))
