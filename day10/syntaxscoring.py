'''
Advent of Code - 2021
Day 10 - Synatx scoring
'''

import statistics

error_score = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

completion_points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

brace_pairs = {'(': ')', '{': '}', '[': ']', '<': '>'}

sum_of_error_scores = 0


def find_error_or_complete(line: str) -> tuple[int, int]:
    '''
    For a given input line, if line contains error then return...
    ...error, or else if line is incomplete return completion score
    '''
    stack = []

    completion_score = 0

    for char in line:
        if char in brace_pairs:
            stack.append(char)
        else:
            if brace_pairs[stack.pop()] != char:
                return error_score[char], 0

    for char in reversed(stack):
        completion_score = (completion_score * 5) + completion_points[brace_pairs[char]]

    return 0, completion_score


with open('input') as input:
    completion_scores = []

    for line in input:
        line = line.strip()
        sum_of_error_score, completion_score = find_error_or_complete(line)

        sum_of_error_scores += sum_of_error_score

        if completion_score > 0:
            completion_scores.append(completion_score)


print(f"Sum of error scores is {sum_of_error_scores}")
print(f"Median of completion scores is {statistics.median(completion_scores)}")
