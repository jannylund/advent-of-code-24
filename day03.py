from utils import parse_file, start_timer, get_time
import re


def sum_multiples(input):
    matches = re.findall(r"mul\((\d+),(\d+)\)", input)
    return sum([int(x) * int(y) for x, y in matches])


def sum_enabled(input):
    # remove everything fron don't to do or don't to $
    input = re.sub(r"don't.*?(do\(\)|$)", "", input)
    return sum_multiples(input)


if __name__ == "__main__":
    example = parse_file("input/ex03.txt")[0]
    example2 = parse_file("input/ex03.txt")[1]
    input = str(parse_file("input/day03.txt"))

    assert sum_multiples(example) == 161

    start = start_timer()
    result = sum_multiples(input)
    print(f"day03p1: sum_multiples {result} in {get_time(start)} ms")
    assert result == 183669043

    assert sum_enabled(example2) == 48

    start = start_timer()
    result = sum_enabled(input)
    print(f"day03p2: sum_enabled {result} in {get_time(start)} ms")
    assert result == 59097164
