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

print_pattern()

def check_win():
    for a in list_win:
        for b in a:
            if player1 != board[b-1]:
                break
            else:
                return True

    return False

for _ in range(9):
    print_board()
    print("player1 turn: ")
    p1 = int(input("player 1 turn "))   # need to add check if empty else no valid
    board[p1-1] = player1
    p2 = int(input("player 2 turn "))
    board[p2-1] = player2
    check_win()





if check_win():

    print("player 1 win ")