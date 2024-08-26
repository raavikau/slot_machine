import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100
ROWS = 3
COLS = 3

symbol_count = {
    "A": 3,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {  # the value of the symbol
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, row_lines, bet, values):
    winning_amount = 0
    winning_lines = []
    for rline in range(row_lines):  # iterate every row by row [ccc],[aba],[ddd]
        symbol = columns[0][rline]  # c, a, d  # c l:0, a 1, d 2 take frst element of every row
        for col in columns:  # col1: cad, cbd, cad take column by column
            symbol_to_check = col[rline]  # c c c, a b, d d d
            if symbol != symbol_to_check:  # a != b
                break
        else:
            winning_amount += values[symbol] * bet  # 3*10 6*10 winning amount with symbol values
            winning_lines.append(rline+1)  # 1 3 append winning lines

    return winning_amount, winning_lines

def get_slot_machine_spin(rows, cols, symbols):  # get random slot machine spin
    all_symbols = []
    for symbol, count in symbols.items():  # take value from symbol_count
        for _ in range(count):  # take value from dictionary irritate over range
            all_symbols.append(symbol)  # add all symbols in list

    columns = []
    for _ in range(cols):  # to the range column
        col = []
        current_symbols = all_symbols[:]  # copy all values
        for _ in range(rows):
            value = random.choice(current_symbols)  # choose value from list
            current_symbols.remove(value)  # remove from list so not come again
            col.append(value)

        columns.append(col)
    return columns

def print_slot_machine(columns):  # print the slot machine
    for row in range(len(columns[0])):  # iterate to the length of column
        for i, column in enumerate(columns):  # take the column one by one
            if i != len(columns) - 1:
                print(column[row], end=' | ')
            else:
                print(column[row])

def deposit():  # to deposit money
    print("Welcome to slot machine simulator")
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number")

    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1 - {MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)  # get the number of lines to bet on
            if 1 <= lines <= MAX_LINES:  # check that the line you choose is in between
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")

    return lines

def get_bet():
    while True:
        bet_amount = input("What would you like to bet on each line? $")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:  # to make sure bet amount is in between
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number")

    return bet_amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet_amount = get_bet()
        total_bet = bet_amount * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is {balance}")
        else:
            break
    print(f"You are betting ${bet_amount} on {lines} lines. Total bet amount is ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet_amount, symbol_value)
    if winnings != 0:
        print(f"You won ${winnings}")
        print("You won on line number:", *winning_lines)  # to show multiple win lines
    else:
        print("You loose")

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        user_input = input("Press enter if you ant to continue (q to quit)").lower()
        if user_input == 'q' or balance == 0:
            break
        result = spin(balance)
        print(f"Result of spin is: {result}")
        balance += result

    print(f"You left with ${balance}")

main()
