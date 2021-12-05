with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

    gamma = ''
    epsilon = ''

    for i in range(0, len(lines[0])):
        count_zero = 0
        count_one = 0
        for line in lines:
            if line[i] == '0':
                count_zero += 1
            else:
                count_one += 1
        if count_zero > count_one:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    gamma_value = int(gamma, 2)
    epsilon_value = int(epsilon, 2)
    power_compsumption = gamma_value * epsilon_value
    
    print(f"Gamma: {gamma} ({gamma_value}); Epsilon: {epsilon} ({epsilon_value}); Power compsumption: {power_compsumption}")
