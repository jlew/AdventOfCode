crab_count = {}

with open('input.txt') as f:
    for init_value in f.readlines()[0].strip().split(','):
        crab_count[int(init_value)] = crab_count.get(int(init_value), 0) + 1

min_index = min(crab_count.keys())
max_index = max(crab_count.keys())
print(f"Crab count: {crab_count}; Range: {min_index} - {max_index}")

best_fuel=None
best_index=0
for target in range(min_index, max_index):
    fuel = 0
    for key in crab_count.keys():
        fuel += abs(key - target) * crab_count[key]
    # print(f"Move all to {target} costs: {fuel}")
    if not best_fuel or fuel < best_fuel:
        best_fuel = fuel
        best_index = target

print(f"Best was {best_fuel} at index {best_index}")
