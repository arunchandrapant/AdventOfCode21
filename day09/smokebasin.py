'''
Advent of Code - 2021
Day 9 - Smoke Basin
'''
import math

basins: list[set] = []


with open('input') as input:
    data: list[list[int]] = []
    for line in input:
        data.append(list(map(int, list(line.rstrip()))))


def find_neighbours(x: int, y: int, max_x: int, max_y: int) -> set:
    '''
    Given a coordinate and max possible values of coordinate
    return a set of all the coordates that are neighbours
    '''
    result = set()
    if x > 0:
        result.add((x - 1, y,))
    if x < max_x:
        result.add((x + 1, y,))
    if y > 0:
        result.add((x, y - 1,))
    if y < max_y:
        result.add((x, y + 1,))

    return result


def find_basins(x: int, y: int, basins: set, data: list[list[int]]) -> None:
    '''
    For a given coordinate, find all neighbours and check if
    neighbour is a part of basin. If it is a part of basin then
    add to basin and recursively call function for this neighbour
    '''
    neighbours = find_neighbours(x, y, len(data) - 1, len(data[0]) - 1)
    curr_val = data[x][y]

    for neighbour in neighbours:
        neighbour_val = data[neighbour[0]][neighbour[1]]
        if curr_val < neighbour_val and neighbour_val < 9 and neighbour not in basins:
            basins.add(neighbour)
            find_basins(neighbour[0], neighbour[1], basins, data)


risk_sum = 0
MAX_X = len(data) - 1
MAX_Y = len(data[0]) - 1

for x in range(0, MAX_X + 1):
    for y in range(0, MAX_Y + 1):
        curr_item = data[x][y]

        neighbours = find_neighbours(x, y, MAX_X, MAX_Y)
        neighbour_values = []

        for neighbour in neighbours:
            neighbour_values.append(data[neighbour[0]][neighbour[1]])

        if curr_item < min(neighbour_values):
            risk_sum += (curr_item + 1)
            basin = {(x, y,)}
            find_basins(x, y, basin, data)
            basins.append(basin)

largest_basins = sorted([len(x) for x in basins], reverse=True)[:3]

print(f"Sum of risk level of all low points is {risk_sum}")
print(f"Product of 3 largest basins is {math.prod(largest_basins)}")
