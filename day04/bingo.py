'''
AOC 2021
Day 4
Bingo - Problem 1 (find winning score) & Problem 2 (find losing score)
'''

with open('input', encoding='utf-8') as input:
    # line containing numbers that are drawn
    nums = list(map(int, input.readline().rstrip().split(",")))
    input.readline()  # waste line
    nums_dict = {num: index for index, num in enumerate(nums)}

    # Store all boards row wise here
    boards = []
    board: list[list[int]] = []
    for line in input:
        if line == '\n':
            boards.append(board)
            board = []
        else:
            board.append(list(map(int, line.rstrip().split())))

    # Store all boards column wise here (obtained after pivoting)
    pivoted_boards = []
    for board in boards:
        new_board = []
        for i in range(0, len(board[0])):
            new_row: list[int] = []
            for row in board:
                new_row.append(row[i])
            new_board.append(new_row)
        pivoted_boards.append(new_board)


def find_winning_position_of_row(row: list[int]) -> int:
    '''
    for a given row or columns, find after how many draws...
    it will be fully marked complete
    '''
    win_pos = -1
    for item in row:
        if item in nums_dict:
            win_pos = max(win_pos, nums_dict[item])
        else:
            win_pos = len(nums)
            break

    return win_pos


# for each board either rowwise or columnwise find after what draws it wins
def find_winning_position_of_board(
        boards: list[list[list[int]]]) -> dict[int, int]:
    '''
    for each board check after how many draws it wins

    this function checks row wise only

    for checking column wise pass pivoted board
    '''
    board_wins: dict[int, int] = {}
    for idx, board in enumerate(boards):
        board_win_pos = len(nums)
        for row in board:
            win_pos = find_winning_position_of_row(row)
            if win_pos < len(nums):
                board_win_pos = min(win_pos, board_win_pos)

        if idx in board_wins:
            board_wins[idx] = min(board_wins[idx], board_win_pos)
        else:
            board_wins[idx] = board_win_pos

    return board_wins


board_wins = find_winning_position_of_board(boards)
board_wins_pivoted = find_winning_position_of_board(pivoted_boards)

min_winning_position = len(nums)
winning_board, max_winning_position, last_winning_board = (-1, -1, -1)

# from board win values extracted row wise and column wise...
# combine them to get final values for winning and losing board
for board_id in range(0, len(boards)):
    win = min(board_wins[board_id], board_wins_pivoted[board_id])
    if win < min_winning_position:
        min_winning_position = win
        winning_board = board_id
    if win > max_winning_position:
        max_winning_position = win
        last_winning_board = board_id


def find_unmarked_sum(board_id: int, winning_pos: int):
    '''
    Find sum of unmarked values in board given winning position
    '''
    winning_nums = set(nums[:winning_pos + 1])
    unmarked_nums = 0
    for row in boards[board_id]:
        for item in row:
            if item not in winning_nums:
                unmarked_nums += item
    return unmarked_nums


print("Winning score is")
print(
    find_unmarked_sum(winning_board, min_winning_position) *
    nums[min_winning_position])

print("Losing score is")
print(
    find_unmarked_sum(last_winning_board, max_winning_position) *
    nums[max_winning_position])
