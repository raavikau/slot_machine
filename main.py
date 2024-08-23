import random

symbol_count = {
    "A": 3,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winning_amount = 0
    winning_lines = []
    for rline in range(lines):
        symbol = columns[0][rline]
        for col in columns:
            symbol_to_check = col[rline]
            if symbol != symbol_to_check:
                break
        else:
            winning_amount += values[symbol] * bet
            winning_lines.append(rline+1)

    return winning_amount, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end='|')
            else:
                print(column[row])

def deposit():
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
        lines = input(f"Enter the number of lines to bet on (1 to 3)? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= 3:
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
            if 1 <= bet_amount <= 100:
                break
            else:
                print("Amount must be between $1 - $100")
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
    print(f"You are betting ${bet_amount} on {lines}. Total bet is equal to ${total_bet}")
    slots = get_slot_machine_spin(3, 3, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet_amount, symbol_value)
    if winnings != 0:
        print(f"You won ${winnings}")
        print("You won on line number:", *winning_lines)
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
