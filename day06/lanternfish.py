'''
AOC 2021
Day 6
Population of lantern fish
'''

from collections import defaultdict
import copy

with open('input') as input:
    initial_fish = list(map(int, input.read().strip().split(",")))

initial_fish_dict = defaultdict(int)

# count of fishes grouped by internal clock state
for item in initial_fish:
    initial_fish_dict[item] += 1

for day in range(0, 256):
    print(initial_fish_dict)
    temp_dict = copy.copy(initial_fish_dict)
    # update state for each day according to rules of fish propogation
    initial_fish_dict[8] = temp_dict[0]
    initial_fish_dict[6] = temp_dict[7] + temp_dict[0]
    initial_fish_dict[7] = temp_dict[8]
    for i in range(0, 6):
        initial_fish_dict[i] = temp_dict[i + 1]

result = 0

for fish, values in initial_fish_dict.items():
    result += values

print(result)
