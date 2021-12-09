'''
Advent Of Code - 2021
Day 7 - The Treachery of Whales
'''

with open('input') as input:
    positions = list(map(int, input.read().strip().split(",")))


def find_fuel_consumption(positions: list[int], meeting_point: int) -> tuple[int, int]:
    '''For a given meeting point, find the fuel consumption for both
    constant and non constant fuel consumption schemes'''
    fuel = 0
    fuel_non_constant = 0
    for pos in positions:
        dist = abs(pos - meeting_point)
        fuel += dist
        fuel_non_constant += ((dist * (dist + 1)) // 2)
    return fuel, fuel_non_constant


min_fuel = sum(positions)
min_fuel_ap = 1e24

for i in range(min(positions), max(positions) + 1):
    fuel, fuel_ap = find_fuel_consumption(positions, i)
    min_fuel = min(fuel, min_fuel)
    min_fuel_ap = min(fuel_ap, min_fuel_ap)

print(f"Minimum fuel spent to align is {min_fuel}")
print(f"Minimum fuel spend to align with non constant fuel burn is {min_fuel_ap}")
