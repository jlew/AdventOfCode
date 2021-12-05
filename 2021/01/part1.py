import sys

last = None
greater_count = 0
for line in sys.stdin:
  lineVal = int(line.rstrip())
  if last:
    if last < lineVal:
      greater_count += 1
  last = lineVal
print(greater_count)
