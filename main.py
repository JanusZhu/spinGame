import random

MAX_LINES = 3
Row = 3
Column = 3
Values = {
    "5":3,
    "2": 2,
    "1": 1
}

def getBalance ():
    while True:
        balance = input("How much do you want to start with? ")
        if balance.isdigit():
            balance = int(balance)
            if balance > 0:
                return balance
            else:
                print("Please enter a valid number")
        else:
            print("Please enter a number") 


def getLine ():
    while True:
        line = input(f"How many lines do you want to bet on (1 - {MAX_LINES})? ")
        if line.isdigit():
            line = int(line)
            if 1 <= line <= MAX_LINES:
                return line
            else:
                print(f"Please enter a valid number. (1 - {MAX_LINES})")
        else:
            print("Please enter a number") 
def getBet(balance):
    while True:
        while True:
            line = getLine()
            bet = input(f"How much do you want to bet on each line? ")
            if bet.isdigit():
                bet = int(bet)
                if 1 <= bet <= balance:
                    break
                else:
                    print(f"Please enter a valid number(1 - {balance})")
            else:
                print("Please enter a number")
        if bet*line > balance:
            print(f"You total bet is {bet*line}, which exceeds your balance {balance}. Please choose another amount!")
        else:
            print(f"You total bet is {bet*line}. Your balance now is {balance - bet*line}.")
            return bet, balance-bet*line, line

def generateSpin (rows, columns, values):
    board = [[] for _ in range(rows)]
    sample = []
    for key, value in values.items():
        for _ in range(value):
            sample.append(key)

    for col in range(columns):
        copy = sample[:]
        print(copy)
        for line in range(rows):
            item = random.choice(copy)
            board[line].append(item)
            copy.remove(item)
    for row in board:
        for i in range(columns):
            if i != columns-1:
                print(row[i], end=" | ")
            else:
                print(row[i], end="")
        print()
    return board

def checkWinning(board, bet, line, balance):
    winningLines = []
    for i in range(line):
        target_item = board[i][0]
        for item in board[i][0:]:
            #print(item, target_item)
            if item != target_item:
                break
        else:
            balance += bet * int(target_item)
            winningLines.append(i)
    print(f"Your current balance is {balance}")
    for i in winningLines:
        print(f"You won the line {i+1}")
    return balance


def main ():
    balance = getBalance()
    while True:
        bet, balance, line = getBet(balance)
        board = generateSpin(Row, Column, Values)
        balance = checkWinning(board,bet,line,balance)
        if balance < 1:
            print("You are broke.")
            break
        data = input("Press Enter to continue? Otherwise press q to quit. ")
        if data == "q":
            print(f"You left with {balance}")
            break

main()