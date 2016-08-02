# Imports
from random import randint
from termcolor import colored


# Setting up and defining the board
board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

print ship_row,ship_col

# Guessing Process
hard = 2
medium = 4
easy = 6

def game():
    user_name = raw_input("What is your name?")

    def input_selection(prompt,choices):
        while True:
            choice = raw_input(prompt)
            if choice in choices:
                return choice
            else:
                print ("That's not valid", choices)

    user_guesses = input_selection("What diffuculty do you want to play at? Hard(2), Medium(4), Easy(6)",('hard', 'medium','easy'))

    if user_guesses == "hard" :
        user_guesses = hard
    elif user_guesses == "medium" :
        user_guesses = medium
    else:
        user_guesses = easy

    # Turn Counter
    for turn in range(user_guesses):
        guesses_taken = turn + 1
        print "Turn", guesses_taken
        guess_row = int(raw_input("Guess Row:"))
        guess_col = int(raw_input("Guess Col:"))

        if (guess_row == ship_row) and (guess_col == ship_col):
            print "Congratulations! You sunk my battleship! It only took", guesses_taken, "turn(s)"
            break
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print "Oops, that's not even in the ocean."

            elif(board[guess_row][guess_col] == "X"):
                print "You guessed that one already."

            else:
                print "You missed my battleship!"
                board[guess_row][guess_col] = colored("X", "red")

            print_board(board)

        if turn == (user_guesses - 1):
            print "Game Over"
            print "In " + guesses_taken + "Guesses"
    scores = user_name, guesses_taken
    write_text = open("leaderboard.txt", "w")
    write_text.write(str(scores))
    write_text.close()
    read_text = open("leaderboard.txt", "r")
    print read_text.read()
    read_text.close()
    re_play = raw_input("Want to play agian?")
    if re_play == "yes":
        game()
        with open("leaderboard.txt", "r+") as textfile:
            textfile.write(scores)
            print leaderboard.txt
    else:
        print "Okay"
game()
