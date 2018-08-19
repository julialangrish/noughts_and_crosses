"""
Just for fun code for naughts and crosses game. Unfinished
Julia Langrish
August 2018
"""

#ideas
##make player class?
##allow different game sizes?
##use sockets for multiplayer


def print_board(board):
    for i in range(3):
        print(board[i][0], board[i][1], board[i][2])
        
def play_turn(player, board):
    played = False
    while not played:
        location = input((player[0]," enter column num, row num sepearted by ',': ")).split(',')
        print(location)
        column = int(location[0]) - 1
        row = int(location[1]) - 1
        print("row {}, column {}".format(row, column))
        if board[column][row] == '_':
            board[column][row] = peice[1]
            played = True
        else:
            print("Invalid location.")
    
    
def main():  
    board = [
        ['_','_','_'],
        ['_','_','_'],
        ['_','_','_']
    ]    
    
    print_board(board)
    curr_player = input("Enter p1 name"), input("p1 choose peice: ")
    next_player = input("Enter p2 name"), input("p2 choose peice: ")
    while True:
        play_turn(curr_player, board)
        print_board(board)
        curr_player, next_player = next_player, curr_player

main()