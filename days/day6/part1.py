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


def main():
    puzzle = read_input("days/day6/input_day6.txt")
    puzzle = puzzle.split("\n\n")

    puzzle = clean_puzzle(puzzle)
    print(get_number_questions(puzzle))
