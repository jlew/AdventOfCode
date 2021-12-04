class Board:
    def __init__(self, input):
        self.board_grid = []
        for line in input:
            self.board_grid.append(line.split())

    def __str__(self):
        str_output = " B  I  N  G  O\n-- -- -- -- --\n"
        for line in self.board_grid:
            str_output += f"{line[0]:>2} {line[1]:>2} {line[2]:>2} {line[3]:>2} {line[4]:>2}\n"
        return str_output

    def is_bingo(self, input):
        # Check Horizontal
        for row in self.board_grid:
            bingo = True
            for column in row:
                if column not in input:
                    bingo = False
            if bingo:
                print(f"BINGO in row: {', '.join(row)}\n{self}")
                return True
        # Check Vertical
        for column in range(0,5):
            bingo = True
            for row in range(0,5):
                if self.board_grid[row][column] not in input:
                    bingo = False
            if bingo:
                print(f"Bingo in column {', '.join([self.board_grid[s][column] for s in range(0,5)])}\n{self}")
                return True

        # Check Diagnals
        # bingo = True
        # for i in range(0,5):
        #     if self.board_grid[i][i] not in input:
        #         bingo = False
        # if bingo:
        #     print(f"Bingo in diagnal {', '.join([self.board_grid[s][s] for s in range(0,5)])}\n{self}")
        #     return True
        #
        # bingo = True
        # for i in range(0,5):
        #     if self.board_grid[4-i][i] not in input:
        #         bingo = False
        # if bingo:
        #     print(f"Bingo in diagnal {', '.join([self.board_grid[4-s][s] for s in range(0,5)])}\n{self}")
        #     return True

        return False
    def get_unmatched_numbers(self, input):
        all_numbers = [item for sublist in self.board_grid for item in sublist]

        return filter( lambda x: x not in input, all_numbers)

def find_winning_board(boards, input):
    for input_count in range(5,len(bingo_numbers)):
        for board in boards:
            bingo_sequence = bingo_numbers[0:input_count]
            if(board.is_bingo(bingo_sequence)):
                print(f"Bingo Sequence: {', '.join(bingo_sequence)}")
                return (board, bingo_sequence)

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

    bingo_numbers = lines.pop(0).split(",")
    print(f"Bingo Sequence: {', '.join(bingo_numbers)}")
    print()

    boards = []
    while lines:
        board = Board(lines[1:6])
        boards.append(board)
        lines = lines[6:]

    (winning_board, sequence) = find_winning_board(boards, bingo_numbers)
    unmatched = winning_board.get_unmatched_numbers(sequence)
    print(sum([int(x) for x in unmatched]) * int(sequence[-1]))




    #print(boards[0].is_bingo(['21','9', '14', '16', '7']))
    #print(boards[0].is_bingo(['17','23', '14', '3', '20']))
    #print(boards[0].is_bingo(['22','2','14','18','19']))
    #print(boards[0].is_bingo(['0','4','14','10','1']))
