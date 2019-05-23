"""
Just for fun code for naughts and crosses game. Unfinished
Julia Langrish
August 2018
Modified May 2019
"""

#ideas
##make player class?
##allow different game sizes?
##use sockets for multiplayer


def print_board(board):
    for i in range(3):
        print(board[i][0], board[i][1], board[i][2])
        
        
def location_checks(location):
    """Returns true if format is correct, false if not"""
    if len(location) != 2:
        return False
    return True
    
    
        
def play_turn(player, board):
    piece = player[1]
    playername = player[0]
    played = False
    while not played:
        location = input("{} enter row num, column num sepearted by space: ".format(playername)).split(' ')
        if location_checks(location):
            column = int(location[0]) - 1
            row = int(location[1]) - 1
            print("row {}, column {}".format(row, column))
            if board[column][row] == '_':
                board[column][row] = piece
                played = True
            else:
                print("Location unavailable. Try again")
        else:
            print("Location invalid. Try again.")
    

def check_win(board):
    """Checks if player has won"""
    pass

    
def main():  
    board = [
        ['_','_','_'],
        ['_','_','_'],
        ['_','_','_']
    ]    
    
    print_board(board)
    curr_player = input("Enter p1 name\n"), input("p1 choose peice: ")
    next_player = input("Enter p2 name\n"), input("p2 choose peice: ")
    while True:
        play_turn(curr_player, board)
        print_board(board)
        check_win(board)
        curr_player, next_player = next_player, curr_player

main()