# tick tack toe game
# create a 2d list for winning combinations
# take user input put it in list and compare 2  list.

list_win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
list_a = []
list_b = []


def print_pattern():
    print("1 | 2 | 3")
    print("__________")
    print("4 | 5 | 6 ")
    print("__________")
    print("6 | 7 | 8 ")


for _ in range(4):
    a = input("A's Turn enter place you want to choose")
    b = input("B's Turn enter place you want to choose")
    list_a.append(int(a))
    list_b.append(int(b))

    if len(list_a) >= 3 or len(list_b) >= 3:
        if list_a in list_win:
            print("player A is winner ")

        if list_b in list_win:
            print("player B is winner ")








