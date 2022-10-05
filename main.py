from curses.ascii import isdigit
from linecache import getline
import random


MAX_LINES = 3

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
def getBet(balance, line):
    while True:
        while True:
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
            return bet




def main ():
    balance = getBalance()
    line = getLine()
    bet = getBet(balance, line)
    print(balance, line, bet)

main()