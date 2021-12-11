class Grid:
    def __init__(self, input):
        self.grid = []
        self.flash_mask = []
        self.grid_height = len(input)
        self.grid_width = len(input[0])
        self.flash_count = 0
        for line in input:
            self.grid.append([int(char) for char in line])
            self.flash_mask.append([False for char in line])

    def __str__(self):
        str_output = ""
        for line in self.grid:
            str_output += f"{''.join([str(val) for val in line])}\n"
        return str_output

    def step(self):
        # Increment and reset flash mask
        for y in range(0, self.grid_height):
            for x in range(0, self.grid_width):
                self.grid[y][x] += 1
                self.flash_mask[y][x] = False

        # Start recursive flash
        for y in range(0, self.grid_height):
            for x in range(0, self.grid_width):
                self._handle_flash(x, y, False)

        # Finsh step
        for y in range(0, self.grid_height):
            for x in range(0, self.grid_width):
                if(self.grid[y][x] > 9):
                    self.grid[y][x] = 0

    def _handle_flash(self, x, y, next_to_flash):
        if(next_to_flash):
            self.grid[y][x] += 1

        # Check if we need to flash Handles (x, y)
        if self.grid[y][x] > 9 and self.flash_mask[y][x] == False:
            self.flash_mask[y][x] = True
            self.flash_count += 1

            # Handles (x,y-1) (x-1,y-1) (x+1,y-1)
            if y-1 != -1:
                self._handle_flash(x, y-1, True)
                if x-1 != -1:
                    self._handle_flash(x-1, y-1, True)

                if x+1 != self.grid_width:
                    self._handle_flash(x+1, y-1, True)

            # Handles (x,y+1) (x-1,y+1) (x+1,y+1)
            if y+1 != self.grid_height:
                self._handle_flash(x, y+1, True)
                if x-1 != -1:
                    self._handle_flash(x-1, y+1, True)

                if x+1 != self.grid_width:
                    self._handle_flash(x+1, y+1, True)

            # Handles (x-y, y) (x+1, y)
            if x-1 != -1:
                self._handle_flash(x-1, y, True)

            if x+1 != self.grid_width:
                self._handle_flash(x+1, y, True)


with open('input.txt') as f:
    grid = Grid([ line.strip() for line in f.readlines()])

    print(grid)
    for step_count in range(1, 100 + 1):
        grid.step()
        print(f"After step {step_count} [{grid.flash_count} flashes]:\n{grid}")
