import re

already_processed = []

def read_input(filename):
    f = open(filename, "r")
    data = f.readlines()
    f.close()
    return data


def get_all_bags(puzzle):
    bags = list()
    content = list()
    for line in puzzle:
        splitted = line.split()
        bags.append(splitted[0] + " " + splitted[1])
        matches = re.findall("\d (\w+ \w+) bag", line)
        number = re.findall("\d", line)
        contains = list()
        if matches:
            for index, element in enumerate(matches):
                contains.append({
                    "color": element,
                    "number": number[index]
                })
        content.append({
            "color": bags[-1],
            "contain": contains
        })
    return bags, content


def golden_bag_in(bag, content, golden_in):
    if bag["color"] != "shiny gold":
        golden_in.append(bag)
    color = bag["color"]
    for element in content:
        for bag in element["contain"]:
            if bag["color"] == color:
                golden_in = golden_bag_in(bag, content, golden_in)
    return golden_in


def test(content, golden_in):
    for bag in content:
        if bag["color"] == "shiny gold":
            pass
        else:
            golden_in = look_into_bags(bag, content, golden_in)
    return golden_in

def look_into_bags(bag, content, golden_in):




def get_number_possibilities(bags, content, searched):
    possibilities = 0
    for index, bag in enumerate(bags):
        if searched == bag:
            possibilities += 1
        else:
            if searched in content[index]["contain"]:
                possibilities += 1
            # else:

#
# def is_target(searched, bag, content):
#     value = False
#     if searched == bag:
#         value = True
#     else:
#         for content[]
#         value = is_target(searched, bag, content)



def main():
    puzzle = read_input("days/day7/example_day7.txt")
    searched = "shiny gold"
    can_contain = list()
    bags, content = get_all_bags(puzzle)
    print(content)
    index_golden = bags.index(searched)
    can_contain = golden_bag_in(content[index_golden], content, can_contain)

    print(can_contain)
    buffer = list()
    for element in can_contain:
        buffer.append(element["color"])

    buffer = list(dict.fromkeys(buffer))

    print(len(buffer))




