def get_o2(starting_lines):
    lines = starting_lines
    for i in range(0, len(lines[0])):
        count_zero = 0
        count_one = 0
        for line in lines:
            if line[i] == '0':
                count_zero += 1
            else:
                count_one += 1

        if count_zero == count_one:
            lines = [line for line in lines if line[i] == '1']
        elif count_zero > count_one:
            lines = [line for line in lines if line[i] == '0']
        else:
            lines = [line for line in lines if line[i] == '1']

        if len(lines) == 1:
            o2 = lines[0]
            o2_value = int(o2, 2)
            print(f"O2: {o2} ({o2_value})")
            return o2_value


def get_co2(starting_lines):
    lines = starting_lines
    for i in range(0, len(lines[0])):
        count_zero = 0
        count_one = 0
        for line in lines:
            if line[i] == '0':
                count_zero += 1
            else:
                count_one += 1

        if count_zero == count_one:
            lines = [line for line in lines if line[i] == '0']
            if(len(lines) == 1):
                co2 = lines[0]
                co2_value = int(co2, 2)
                print(f"CO2: {co2} ({co2_value})")
                return co2_value
        elif count_zero > count_one:
            lines = [line for line in lines if line[i] == '1']
        else:
            lines = [line for line in lines if line[i] == '0']

        if len(lines) == 1:
            o2 = lines[0]
            o2_value = int(o2, 2)
            print(f"O2: {o2} ({o2_value})")
            return o2_value


with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

    print(f"Life Support Remaining: {get_o2(lines) * get_co2(lines)}")
