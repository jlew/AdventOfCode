with open('input.txt') as f:
    lines = [ line.strip().split(' | ') for line in f.readlines()]

    count = 0
    for (input, output) in lines:
        output_segments = output.split(" ")
        segment_lengths = [len(l) for l in output_segments]
        for length in segment_lengths:
            if length in [2, 4, 3, 7]:
                count += 1
    print(count)
