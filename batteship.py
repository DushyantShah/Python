from random import randint
from random import choice

global user_board
user_board = []
global comp_board
comp_board = []
global user_guess_board
user_guess_board = []


# Create 3 battleship boards
def create_board():
	for x in range(5):
		user_board.append(['0'] * 5)
		comp_board.append(['0'] * 5)
		user_guess_board.append(['0'] * 5)


# Function to print Player 1's board
def print_user_board():
	print "---------------"
	print "Player 1 board"
	print "---------------"
	for row in user_board:
		print " ".join(row)


# Function to print Player 1's guesses
def print_user_guess_board():
	print "---------------"
	print "Player 1's guesses"
	print "---------------"
	for row in user_guess_board:
		print " ".join(row)


# Function to print the computer's board
def print_comp_board():
	print "---------------"
	print "Computer board"
	print "---------------"
	for row in comp_board:
		print " ".join(row)


# Function to check a board if the battleship has sunk
def checkWinner(board):
	for x in range(len(board)):
		for y in range(len(board[0])):
			if board[x][y] == "B":
				return False
	return True


# Function to place battleship on board for Player 1 and Computer
def place_ship(player):
	battleship_nofit = True
	if player == user_board:
		x = 100
		y = 100
		orientation = "X"
		while battleship_nofit:
			while x > 4:
				try:
					x = abs(int(raw_input("X coordinate of your battleship [0-4]:")))
				except ValueError:
					print ("Invalid input. Please try again.")
			while y > 4:
				try:
					y = abs(int(raw_input("Y coordinate of your battleship [0-4]:")))
				except ValueError:
					print ("Invalid input. Please try again.")
			while orientation != "V" and orientation != "H":
				orientation = str(raw_input("Orientation - Vertical(V) or Horizontal(H):")).upper()
			# print orientation
			if orientation == "H" and x + 3 > 5:
				print ("Please re-enter your coordinates as your battleship does not fit on the board")
				x = 100
				y = 100
				orientation = "X"
			elif orientation == "V" and y + 3 > 5:
				print ("Please re-enter your coordinates as your battleship does not fit on the board")
				x = 100
				y = 100
				orientation = "X"
			else:
				battleship_nofit = False
	else:
		x = randint(0, len(player) - 3)
		y = randint(0, len(player[0]) - 3)
		orientation = str(choice(["v", "h"])).upper()

	if orientation == "V":
		for i in range(x, x + 3):
			player[i][y] = "B"
	else:
		for i in range(y, y + 3):
			player[x][i] = "B"


def play_game():
	winner = "Nobody"
	turn = "player1"
	print "\n---------------"
	print("Let's play Battleship")
	print "---------------"
	while winner == "Nobody":
		if turn == "player1":
			# Requesting player 1 to make a guess
			while True:
				guesses = raw_input("\nPlease enter your guess (Format: row col) - ").split()
				if len(guesses) != 2:
					print("You have not entered 2 values. Please try again")
					continue
				else:
					try:
						guess_row = abs(int(guesses[0]))
						guess_col = abs(int(guesses[1]))
					except ValueError:
						print("Invalid input. Please try again.")
					else:
						if guess_row > 4 or guess_col > 4:
							print("You coordinates are outside of the board.Please try again.")
						elif user_guess_board[guess_row][guess_col] == "o" or user_guess_board[guess_row][guess_col] == "X":
							print("You have already tried these coordinates. Please try again.")
						else:
							break
			if comp_board[guess_row][guess_col] == "B":
				print player_one + " guessed [" + str(guess_row) + "," + str(
					guess_col) + "] and that was a hit! Good job!"
				user_guess_board[guess_row][guess_col] = "X"
				comp_board[guess_row][guess_col] = "X"

			else:
				print "Oh sorry! " + player_one + " guessed [" + str(guess_row) + "," + str(
					guess_col) + "] and that was miss."
				user_guess_board[guess_row][guess_col] = "o"
				comp_board[guess_row][guess_col] = "o"
			print_user_guess_board()
			turn = "computer"
		# Computer's turn to make a guess
		else:
			guess_row = randint(0, len(user_board) - 1)
			guess_col = randint(0, len(user_board) - 1)
			if user_board[guess_row][guess_col] == "B":
				print "Oh the computer guessed [" + str(guess_row) + "," + str(guess_col) + "] and hit your battleship!"
				user_board[guess_row][guess_col] = "X"
			else:
				print "The computer guessed [" + str(guess_row) + "," + str(guess_col) + "] and missed your battleship"
				user_board[guess_row][guess_col] = "o"
			print_user_board()
			turn = "player1"
		# Once a turn is played, check for a winner
		if (checkWinner(comp_board)):
			winner = "Player1"
		elif (checkWinner(user_board)):
			winner = "Computer"
	# Congratulate the winner
	if winner == "Player1":
		print "Congratulations! You won"
	else:
		print "I am sorry you lost"


global player_one
player_one = raw_input("Enter your name:")
print "Hello " + player_one + "! Welcome to BattleShip"

create_board()
place_ship(user_board)
place_ship(comp_board)
print_user_board()
print_user_guess_board()
play_game()
