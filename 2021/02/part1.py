horizontal = 0
depth = 0
with open('input.txt') as f:
    for line in f.readlines():
        (direction, distance) = line.strip().split(" ")

        if direction == 'forward':
            horizontal += int(distance)

        elif direction == 'down':
            depth += int(distance)

        elif direction == 'up':
            depth -= int(distance)

    print(horizontal,depth,horizontal*depth)
