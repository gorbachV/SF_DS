
def echo_credits():
    print("Practice task: 'XO-game'")
    print(" 29/05/2021 by Kiril Avdeev")


def get_presentation(turn_):
    presentations_ = ('', 'X', 'O', '-')
    return presentations_[turn_]


def echo_playground(game_state_):
    print("     1 | 2 | 3")
    print("  A ", get_presentation(game_state_[0][0]), "|", get_presentation(game_state_[0][1]), "|", get_presentation(game_state_[0][2]))
    print("  B ", get_presentation(game_state_[1][0]), "|", get_presentation(game_state_[1][1]), "|", get_presentation(game_state_[1][2]))
    print("  C ", get_presentation(game_state_[2][0]), "|", get_presentation(game_state_[2][1]), "|", get_presentation(game_state_[2][2]))


def input_turn(turn_):
    prompt = "\nPlease input place where '" + get_presentation(turn_) + "' should be: "
    return input(prompt)


def validate_place(place_):
    valid_row_code = ('A', 'B', 'C')
    valid_col_code = ('1', '2', '3')

    if len(place_) == 2 and place_[0] in valid_row_code and place_[1] in valid_col_code:
        return True
    else:
        return False


def get_coordinates(place_):
    valid_row_code = ('A', 'B', 'C')
    valid_col_code = ('1', '2', '3')

    row = valid_row_code.index(place_[0])
    col = valid_col_code.index(place_[1])

    return row, col


def make_turn(game_state_, place_, turn_):
    row_, col_ = get_coordinates(place_)

    if game_state_[row_][col_] == -1:
        game_state_[row_][col_] = turn_
        return True
    else:
        return False


def check_combination_for_win(combination_):
    winner_is_ = combination_[0]
    win_combination_ = [winner_is_] * 3

    if winner_is_ > 0 and combination_ == win_combination_:
        return winner_is_
    else:
        return -1


def check_winner(game_state_, place_):
    row_number_, col_number_ = get_coordinates(place_)
    row_ = game_state_[row_number_]
    winner_is_ = check_combination_for_win(row_)
    if winner_is_ > 0:
        return winner_is_
    
    col_ = [game_state[i][col_number_] for i in range(3)]
    winner_is_ = check_combination_for_win(col_)
    if winner_is_ > 0:
        return winner_is_
    
    diagonal_indexes_ = [0, 1, 2]
    if row_number_ in diagonal_indexes_ and col_number_ in diagonal_indexes_:
        diagonal_ = [game_state[i][i] for i in range(3)]
        winner_is_ = check_combination_for_win(diagonal_)
        if winner_is_ > 0:
            return winner_is_

        diagonal_ = [game_state[i][(i + 1) * -1] for i in range(3)]
        return check_combination_for_win(diagonal_)
    
    return -1


if __name__ == '__main__':
    echo_credits()

    game_state = [[-1] * 3 for _ in range(3)]

    turn, winner_is, turns_qty = 1, -1, 0
    while winner_is < 0 and turns_qty < 9:
        echo_playground(game_state)

        place = None
        cur_turn_is_valid = False
        while not cur_turn_is_valid:
            place = input_turn(turn)
            if not validate_place(place):
                print("Place is wrong")
            elif not make_turn(game_state, place, turn):
                print("Place is busy")
            else:
                cur_turn_is_valid = True

        turn = 1 if turn == 2 else 2
        turns_qty += 1
        if turns_qty > 4:
            winner_is = check_winner(game_state, place)

    echo_playground(game_state)
    if winner_is > 0:
        print("'" + get_presentation(winner_is) + "' WINS!")
    else:
        print("DRAW!")

