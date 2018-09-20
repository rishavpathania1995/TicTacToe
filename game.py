# tick tack toe game
# create a 2d list for winning combinations
# take user input put it in list and compare 2  list.

list_win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
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
    print(f"Turn of player: {player}")

    position = input("enter position")

    if position.isdigit():                         # check if digit
        position = int(position)
        if board[position-1] == " ":               # check if empty

            #board[position-1] = player

            if 0 <= position <= 9:                 # check if b/w 0-9
                board[position-1] = player

            else:
                print("Please enter between 1 - 9")
                input_value(player)
        else:
            print("Please Choose empty position")
            input_value(player)
    else:
        print("Please enter interger position between 1-9")
        input_value(player)


def win(player):

    for wincombo in list_win:
        for w in wincombo:
            if player != board[w - 1]:  # for else statement else only runs if for doest break
                break
        else:
            return True
    return False


def main():
    counter = 8
    while counter:
        input_value(player1)
        print_board()
        if win(player1):
            print("Player 1 win !!!!")
            break
        input_value(player2)
        if win(player2):
            print("Player 2 win !!!!")
            break

        print_board()
        counter -= 1


if __name__ == "__main__":

    main()