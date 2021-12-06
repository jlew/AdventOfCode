age_group = { 8: 0, 7:0, 6:0, 5:0, 4:0, 3:0, 2:0, 1:0, 0:0}

with open('input.txt') as f:

    for init_value in f.readlines()[0].strip().split(','):
        age_group[int(init_value)] += 1

    print(f"Initial State: {age_group}")
    for day in  range(1,256+1):
        age_group[8], age_group[7], age_group[6],\
        age_group[5], age_group[4], age_group[3],\
        age_group[2], age_group[1], age_group[0] = \
        age_group[0], age_group[8], age_group[7] + age_group[0],\
        age_group[6], age_group[5], age_group[4],\
        age_group[3], age_group[2], age_group[1]

        print(f"Processing day {day}")

    print(f"Total fish after {day} days: {sum(age_group.values())}")
