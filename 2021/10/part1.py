score_values = {
    ')': 3, ']': 57, '}': 1197, '>' : 25137
}

opening_value = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>'
}
with open('input.txt') as f:
    lines = [ line.strip() for line in f.readlines()]

    broken_score = 0
    for line in lines:
        stack = []
        for char in line:
            if char in opening_value.keys():
                stack.append(char)
            else:
                actual_value = char
                expected_value = opening_value[stack.pop()]
                if not expected_value == actual_value:
                    broken_score += score_values[actual_value]
                    print(f"\tExpected {expected_value}, but found  {actual_value} instead.")
                    break

    print( broken_score )
