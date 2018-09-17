# tick tack toe game
# create a 2d list for winning combinations
# take user input put it in list and compare 2  list.

list_win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

board = [" "," "," "," "," "," "," "," "," "]
player1 = "X"
player2 = "O"


def print_pattern():
    print("1 | 2 | 3")
    print("__________")
    print("4 | 5 | 6 ")
    print("__________")
    print("6 | 7 | 8 ")


def print_board():
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("---------------------")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("---------------------")
    print(f"{board[6]}|{board[7]}|{board[8]}")


def input_value(player):

    position = input("enter position")
    if board[position-1] == " " and 1 <= position <= 9 and position.isdigit():
        board[position-1] = player

    else:
        print("please enter correct position")
        input_value(player)


def win(player):
    for wincombo in list_win:
        for w in wincombo:
            if player != board[w - 1]:
                break
            else:
                return True
            #return True
    return False


def main():
    counter = 9
    while counter:
        input_value(player1)
        print_board()
        input_value(player2)
        print_board()

    else:
        print("turn over")

        counter -= 1





main()