import sys

def number_board():
    print("      1|2|3")
    print("      -+-+-")
    print("      4|5|6")
    print("      -+-+-")
    print("      7|8|9")

def current_board():
    global theBoard
    print("      " + theBoard['top-L'] + '|' + theBoard['top-M'] + '|' + theBoard['top-R'])
    print("      " + '-+-+-')
    print("      " + theBoard['mid-L'] + '|' + theBoard['mid-M'] + '|' + theBoard['mid-R'])
    print("      " + '-+-+-')
    print("      " + theBoard['low-L'] + '|' + theBoard['low-M'] + '|' + theBoard['low-R'])

def input_xo_into_dictionary(num, xo):
    global theBoard
    if num == 1:
        theBoard.update({'top-L' : xo})
    elif num == 2:
        theBoard.update({'top-M' : xo})
    elif num == 3:
        theBoard.update({'top-R' : xo})
    elif num == 4:
        theBoard.update({'mid-L' : xo})
    elif num == 5:
        theBoard.update({'mid-M' : xo})
    elif num == 6:
        theBoard.update({'mid-R' : xo})
    elif num == 7:
        theBoard.update({'low-L' : xo})
    elif num == 8:
        theBoard.update({'low-M' : xo})
    elif num == 9:
        theBoard.update({'low-R' : xo})

def define_number_to_position(num):
    if num == 1:
        return 'top-L'
    elif num == 2:
        return 'top-M'
    elif num == 3:
        return 'top-R'
    elif num == 4:
        return 'mid-L'
    elif num == 5:
        return 'mid-M'
    elif num == 6:
        return 'mid-R'
    elif num == 7:
        return 'low-L'
    elif num == 8:
        return 'low-M'
    elif num == 9:
        return 'low-R'

def check_match():
    global theBoard
    if ('X' or 'O') in theBoard['top-L'] and ('X' or 'O') in theBoard['mid-M'] and ('X' or 'O') in theBoard['low-R']:
        return True
    elif ('X' or 'O') in theBoard['top-R'] and ('X' or 'O') in theBoard['mid-M'] and ('X' or 'O') in theBoard['low-L']:
        return True
    elif ('X' or 'O') in theBoard['top-L'] and ('X' or 'O') in theBoard['mid-L'] and ('X' or 'O') in theBoard['low-L']:
        return True
    elif ('X' or 'O') in theBoard['top-M'] and ('X' or 'O') in theBoard['mid-M'] and ('X' or 'O') in theBoard['low-M']:
        return True
    elif ('X' or 'O') in theBoard['top-R'] and ('X' or 'O') in theBoard['mid-R'] and ('X' or 'O') in theBoard['low-R']:
        return True
    elif ('X' or 'O') in theBoard['top-L'] and ('X' or 'O') in theBoard['top-M'] and ('X' or 'O') in theBoard['top-R']:
        return True
    elif ('X' or 'O') in theBoard['mid-L'] and ('X' or 'O') in theBoard['mid-M'] and ('X' or 'O') in theBoard['mid-R']:
        return True
    elif ('X' or 'O') in theBoard['low-L'] and ('X' or 'O') in theBoard['low-M'] and ('X' or 'O') in theBoard['low-R']:
        return True
    else:
        return False

def ask_for_number(alphabet):
    global theBoard
    while True:
        number = input(f"Input a number 1 to 9 to place {alphabet} in one of the nine squares: ")
        if number.isnumeric() == True:
            number = int(number)
            if number >= 10 or number <= 0:
                continue
            else:
                position = define_number_to_position(number)
                if 'X' in theBoard[position]:
                    continue
                elif 'O' in theBoard[position]:
                    continue
                else:
                    break
    return number

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ',
            'low-M': ' ', 'low-R': ' '}
print("Starting Tic Tac Toe")
round = 0
while round <= 9:
    # X
    number_board()
    print()
    current_board()
    number = ask_for_number("X")
    input_xo_into_dictionary(number, "X")
    if check_match() == True:
        number_board()
        print()
        current_board()
        print()
        print("X wins.")
        sys.exit()
    round += 1
    if round == 9:
        number_board()
        current_board()
        break
    # O
    number_board()
    print()
    current_board()
    number = ask_for_number("O")
    input_xo_into_dictionary(number, "O")
    if check_match() == True:
        number_board()
        current_board()
        print()
        print("O wins.")
        sys.exit()
    round += 1
    if round == 9:
        number_board()
        current_board()
        break
print("Both tie.")