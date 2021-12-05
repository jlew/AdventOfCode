
last = [0,0,0]
greater_count = 0
with open('input.txt') as f:
    for line in f.readlines():
      lineVal = int(line.rstrip())
      if len(last) > 5:
        window_sum = sum(last[-4:-1])
        window2_sum = sum(last[-3:])
        if window_sum < window2_sum:
          print("Increased")
          greater_count += 1
        elif window_sum == window2_sum:
          print("SAME")
        else:
          print("Decreased")
        print(" + ".join(map(str,last[-4:-1])),"=",window_sum,"     "," + ".join(map(str, last[-3:])),"=",window2_sum)
      last.append(lineVal)
    print(greater_count)
