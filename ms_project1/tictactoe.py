def get_player_name(num):
    # print(f"Getting player details")
    return input(f"Enter name of play {num}: ")


def get_first_player(p1, p2):
    # print(f"Getting first player")
    player_name = ''
    print(f"{p1[0]} and {p2[0]}")

    while player_name not in [p1[0], p2[0]]:
        player_name = input(f"Who wants to go first, {p1[0]} or {p2[0]}: ")
    return player_name


def draw_board(board):
    print(f"7  |8  |9  ")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print(f"   |   |   ")
    print(f"___________")
    print(f"4  |5  |6  ")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print(f"   |   |   ")
    print(f"___________")
    print(f"1  |2  |3  ")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print(f"   |   |   ")


def reset_board(board):
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    return board


def position_clear(pos, myboard):
    idx = int(pos) - 1
    if myboard[idx] == ' ':
        return True
    else:
        return False


def make_move(player, pos, myboard):
    idx = int(pos) - 1
    myboard[idx] = player[1]
    return myboard


def take_turn(current_player, p1, p2):
    if current_player[0] == p1[0]:
        return p2
    else:
        return p1


def is_winner(myboard):
    winning_board = [
        [myboard[0], myboard[1], myboard[2]],
        [myboard[3], myboard[4], myboard[5]],
        [myboard[6], myboard[7], myboard[8]],
        [myboard[0], myboard[3], myboard[6]],
        [myboard[1], myboard[4], myboard[7]],
        [myboard[2], myboard[5], myboard[8]],
        [myboard[0], myboard[4], myboard[8]],
        [myboard[2], myboard[4], myboard[6]]
    ]
    if ['X', 'X', 'X'] in winning_board or ['O', 'O', 'O'] in winning_board:
        return True
    else:
        return False


if __name__ == '__main__':
    print(f"\n*** Welcome to the Tictactoe Game")

    myboard = ['X', 'O', 'X', 'X', 'O', 'X', 'X', 'O', 'X']
    player1 = ['Player 1', 'X']
    player2 = ['Player 2', 'O']

    # get player details
    player1[0] = get_player_name(1)
    player2[0] = get_player_name(2)

    # choose who wants to start
    current_player_name = get_first_player(player1, player2)
    if current_player_name == player1[0]:
        current_player = player1
    else:
        current_player = player2

    # draw_board
    myboard = reset_board(myboard)

    # play game until game over
    game_on = True
    while game_on:
        draw_board(myboard)
        pos = input(f"Enter a position 1 - 9 {current_player[0]}: ")
        if int(pos) not in range(1, 9):
            continue
        if position_clear(pos, myboard):
            myboard = make_move(current_player, pos, myboard)
            if is_winner(myboard):
                game_on = False
                break
        else:
            print(f"Position is taken {current_player[0]}")
            continue
        current_player = take_turn(current_player, player1, player2)

    # declare the result
    draw_board(myboard)
    print(f"\n *** {current_player[0]} *** is the winner of this round..!")
