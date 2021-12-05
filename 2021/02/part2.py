horizontal = 0
depth = 0
aim = 0
with open('input.txt') as f:
    for line in f.readlines():
        (direction, distance) = line.strip().split(" ")

        if direction == 'forward':
            horizontal += int(distance)
            depth += aim * int(distance)

        elif direction == 'down':
            aim += int(distance)

        elif direction == 'up':
            aim -= int(distance)

    print(horizontal,depth,horizontal*depth)
