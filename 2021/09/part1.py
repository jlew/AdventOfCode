class Grid:
    def __init__(self, input):
        self.grid = []
        self.grid_height = len(input)
        self.grid_width = len(input[0])
        for line in input:
            self.grid.append([int(char) for char in line])

    def __str__(self):
        str_output = ""
        for line in self.grid:
            str_output += f"{''.join([str(val) for val in line])}\n"
        return str_output

    def find_local_minimums(self):
        local_minimums = []
        for y in range(0, self.grid_height):
            for x in range(0, self.grid_width):
                current_val = self.grid[y][x]

                if      (True if y-1 == -1               else current_val < self.grid[y-1][x]) \
                    and (True if y+1 == self.grid_height else current_val < self.grid[y+1][x]) \
                    and (True if x-1 == -1               else current_val < self.grid[y][x-1]) \
                    and (True if x+1 == self.grid_width  else current_val < self.grid[y][x+1]):
                    local_minimums.append(current_val)
        return local_minimums

with open('input.txt') as f:
    grid = Grid([ line.strip() for line in f.readlines()])

    print(grid)
    local_min = grid.find_local_minimums()
    print(local_min)
    print(sum([x+1 for x in local_min]))
