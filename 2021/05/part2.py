from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
PointValue = namedtuple("PointValue", ["point", "value"])

class PlayField:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.grid = []

        for x in range(0,height):
            self.grid.append([ 0 ] * width)

    def plot(self, start, end):
        if start.x == end.x:
            # process delta in y
            if start.y > end.y:
                start, end = end, start
            for y in range(start.y, end.y+1):
                self.grid[y][start.x] += 1
        elif start.y == end.y:
            # process delta in x
            if start.x > end.x:
                start, end = end, start
            for x in range(start.x, end.x+1):
                self.grid[start.y][x] += 1
        else:
            # Make sure that x is increasing so we only have to process 2 types
            # of diagnals
            if end.x < start.x:
                start, end = end, start

            # Y increasing
            if end.y > start.y:
                for i in range(0, end.y - start.y + 1):
                        self.grid[start.y+i][start.x+i] += 1
            else:
                for i in range(0, start.y - end.y + 1):
                        self.grid[start.y-i][start.x+i] += 1

    def get_points(self, filter=lambda x: True):
        points = []
        for x in range(0,self.height):
            for y in range(0,self.width):
                if filter(self.grid[y][x]):
                    points.append(PointValue(Point(x,y), self.grid[y][x]))
        return points

    def __str__(self):
        output = ""
        for x in range(0,self.height):
            for y in range(0,self.width):
                output += '.' if self.grid[x][y] == 0 else str(self.grid[x][y])
            output += '\n'
        return output

with open('input.txt') as f:
    field = PlayField(1000,1000)

    lines = [line.strip().split(' -> ') for line in f.readlines()]
    for line in lines:
        start = line[0].split(",")
        end = line[1].split(",")
        field.plot(Point(int(start[0]),int(start[1])), Point(int(end[0]),int(end[1])))

    print(field)
    points_overlapped = field.get_points(lambda value: value >= 2)
    #new_line_tab = '\n   * '
    #print(f"Points Overlapped:{new_line_tab}{new_line_tab.join([f'{x.point.x}, {x.point.y}: {x.value}'  for x in points_overlapped])}")
    print(f"Points Overlapped Count: {len(points_overlapped)}")
