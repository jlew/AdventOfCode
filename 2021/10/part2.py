score_values = {
    ')': 1, ']': 2, '}': 3, '>' : 4
}

opening_value = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>'
}

with open('input.txt') as f:
    lines = [ line.strip() for line in f.readlines()]

    scores = []

    for line in lines:
        stack = []
        invalid = False
        for char in line:
            if char in opening_value.keys():
                stack.append(char)
            else:
                actual_value = char
                expected_value = opening_value[stack.pop()]
                if not expected_value == actual_value:
                    invalid = True
                    break
        if len(stack) and not invalid:
            incomplete_score = 0
            for char in stack[::-1]:
                incomplete_score = incomplete_score * 5
                incomplete_score += score_values[opening_value[char]]
            scores.append(incomplete_score)

            print(f"Line Incomplete: {line} :: {''.join(stack)}")

    scores.sort()
    # print(scores)
    print(scores[int(len(scores)/2)])
