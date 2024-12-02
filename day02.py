from utils import *


def parse_input(input):
    levels = []
    for line in input:
        report = list(map(int, line.split()))
        levels.append(report)
    return levels


def is_safe(report):
    sorted_report = sorted(report)
    if not sorted_report in [report, report[::-1]]:
        return False

    for i in range(len(sorted_report)):
        if i > 0:
            diff = sorted_report[i] - sorted_report[i-1]
            if diff < 1 or diff > 3:
                return False
    return True


def is_safe_damper(report):
    for i in range(len(report)):
        if is_safe(report[:i] + report[i+1:]):
            return True
    return False


def get_safereports(input):
    report = parse_input(input)
    safe = 0
    for r in report:
        if is_safe(r):
            safe += 1
    return safe


def get_safereports_with_damper(input):
    report = parse_input(input)
    safe = 0
    for r in report:
        if is_safe_damper(r):
            safe += 1
    return safe


if __name__ == "__main__":
    example = parse_file("input/ex02.txt")
    input = parse_file("input/day02.txt")


    assert get_safereports(example) == 2

    start = start_timer()
    safe_reports = get_safereports(input)
    print(f"day02p1: safe reports {safe_reports} in {get_time(start)} ms")
    assert safe_reports == 202


    assert get_safereports_with_damper(example) == 4

    start = start_timer()
    safe_reports = get_safereports_with_damper(input)
    print(f"day02p2: safe reports with damper {safe_reports} in {get_time(start)} ms")
    assert safe_reports == 271
