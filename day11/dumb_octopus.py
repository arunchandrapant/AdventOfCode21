'''
Advent of Code - 2021
Day 11 - Dumbo Octopus
'''
with open('input') as input:
    data: list[list[int]] = []
    data.append([-1]*12)  # guard values
    for line in input:
        # including guard values in row
        data.append([-1] + [int(x) for x in line.strip()] + [-1])
    data.append([-1]*12)  # guard values


def increment_and_propogate(data: list[list[int]]) -> int:
    '''
    Iterate through each vlaue in data one by one and increment it.
    If after increment value is greater than 9, then propogate value to neighbours.
    For > 9 values encountered during iteration or propogation, keep it's postion in store.
    After iteration and propogation set data corresponding to each position in store to zero
    '''
    bright_pos = set()
    for y in range(1, 11):
        for x in range(1, 11):
            if data[y][x] == 9:
                data[y][x] += 1
                bright_pos.add((y, x,))
                propagate(y, x, data, bright_pos)
            else:
                data[y][x] += 1

    for y, x in bright_pos:
        data[y][x] = 0

    return len(bright_pos)


diff = {0, 1, -1}

def propagate(y: int, x: int, data: list[list[int]], bright_pos: set[tuple[int, int]]):
    '''
    For each position, find neighbour and add one to value.
    If neighbour value becomes > 9, then add neighbours position to store...
    ... and recursively call propagate for neighbour
    '''
    for dx in diff:
        for dy in diff:
            neighbour = data[y + dy][x + dx]
            if neighbour == -1:
                pass
            elif neighbour == 9:
                data[y + dy][x + dx] += 1
                bright_pos.add((y + dy, x + dx, ))
                propagate(y + dy, x + dx, data, bright_pos)
            else:
                data[y + dy][x + dx] += 1

total_flashes = 0
all_flash_step = 0
loops = 1

while True:
    flashes = increment_and_propogate(data)
    if loops <= 100:
        total_flashes += flashes
    elif all_flash_step != 0:
        break

    if flashes == 100:
        if all_flash_step == 0:
            all_flash_step = loops
    loops += 1


print(f"Total number of flashes in first 100 iterations is {total_flashes}")
print(f"Step number at which all positions flash is {all_flash_step}")
