
with open('input') as input:
    data = []
    data.append([-1]*12)
    for line in input:
        data.append([-1] + [int(x) for x in line.strip()] + [-1])
    data.append([-1]*12)


def increment_and_propogate(data):
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

def propagate(y, x, data, bright_pos):
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


print(total_flashes)
print(all_flash_step)
