
global p1_board
p1_board = [' ']*9
global player2_board
player2_board = [' ']*9
global comp_board
comp_board = [' ']*9

print("-----------------------")
print("Welcome to Tic-Tac-Toe")
print("-----------------------")

def sample_board():
    print("7|8|9")
    print("-+-+-")
    print("4|5|6")
    print("-+-+-")
    print("1|2|3")

def display_board():
    print(p1_board[6]+"|"+p1_board[7]+"|"+p1_board[8])
    print("-+-+-")
    print(p1_board[3]+"|"+p1_board[4]+"|"+p1_board[5])
    print("-+-+-")
    print(p1_board[0]+"|"+p1_board[1]+"|"+p1_board[2])

sample_board()
display_board()
