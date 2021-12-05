'''
AOC 2021
Day 5
Hydrothermal vents
'''

from collections import defaultdict

input = open('input')

# store points and overlap counts in horiontal or vertical lines
points_dict = defaultdict(int)
# store points and overlap counts in horizontal, vertical and diagonal lines
diagnoal_points_dict = defaultdict(int)

for line in input:
    # for each line find coordinates of points
    process = lambda x: int(str.strip(x))
    x1, y1, x2, y2 = tuple(
        map(process,
            line.strip().replace("->", ",").split(",")))
    minx, maxx, miny, maxy = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)

    # points in horizontal line
    if x1 == x2:
        for y in range(miny, maxy + 1):
            points_dict[(
                x1,
                y,
            )] += 1
            diagnoal_points_dict[(
                x1,
                y,
            )] += 1
    # points in vertical lines
    elif y1 == y2:
        for x in range(minx, maxx + 1):
            points_dict[(
                x,
                y1,
            )] += 1
            diagnoal_points_dict[(
                x,
                y1,
            )] += 1
    # points in diagonal lines
    elif abs(x1 - x2) == abs(y1 - y2):
        # lines with positive slope
        if (x1 < x2 and y1 < y2) or (x2 < x1 and y2 < y1):
            tminx, tminy = minx, miny
            while tminx <= maxx:
                diagnoal_points_dict[(
                    tminx,
                    tminy,
                )] += 1
                tminx += 1
                tminy += 1
        # lines with negative slope
        else:
            tminx, tmaxy = minx, maxy
            while tminx <= maxx:
                diagnoal_points_dict[(
                    tminx,
                    tmaxy,
                )] += 1
                tminx += 1
                tmaxy -= 1

print("Overlap points")
print(sum([1 for x, y in points_dict.items() if y > 1]))
print("Overlap points with diagonal included")
print(sum([1 for x, y in diagnoal_points_dict.items() if y > 1]))

input.close()
