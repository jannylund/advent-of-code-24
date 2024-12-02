from utils import *

def parse_input(input):
    col1, col2 = [], []
    for line in input:
        c1, c2 = map(int, line.split())
        col1.append(c1)
        col2.append(c2)
    return col1, col2


def calculate_distance(input):
    col1, col2 = parse_input(input)
    sorted_col1 = sorted(col1)
    sorted_col2 = sorted(col2)
    total_distance = 0
    for i in range(len(sorted_col1)):
        total_distance += abs(sorted_col1[i] - sorted_col2[i])
    return total_distance


def similarity_score(input):
    left, right = parse_input(input)
    score = 0
    for i in range(len(left)):
        score += left[i] * right.count(left[i])
    return score


if __name__ == "__main__":
    example = parse_file("input/ex01.txt")
    input = parse_file("input/day01.txt")


    assert calculate_distance(example) == 11

    start = start_timer()
    distance = calculate_distance(input)
    assert distance == 3714264
    print(f"day01p1: total distance {distance} in {get_time(start)} ms")


    assert similarity_score(example) == 31

    start = start_timer()
    score = similarity_score(input)
    print(f"day01p2: similarity score {score} in {get_time(start)} ms")
    assert score == 18805872