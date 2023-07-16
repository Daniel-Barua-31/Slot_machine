import random



MAX_LINES = 3 #Constant value or Global value.
MAX_BET = 100
MIN_BET = 0

ROWS = 3 
COLS = 3 

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8,
}

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2,
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows,cols,symbols) :
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)
    columns = []
    for col in range (cols) :
        column = []
        current_symbols = all_symbols[:]
        
        for row in range (rows) :
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns): 
            if i  != len(columns)-1 :
                print(column[row], end=" | ")
            else :
                print(column[row], end="")
        print() 


def deposit() :
    while True : 
        amount = input("Enter How much money you want to spent : $")
        if amount.isdigit() :
            amount = int(amount)
            if  amount > 0 :
                break
            else :
                print("Enter a Postive Number.")
        else :
            print ("Please enter a number")
    return amount

def get_number_lines() :
    while True : 
        lines = input("Enter a number of lines that you want to bet on : (1-"+ str(MAX_LINES)+") ?")
        if lines.isdigit() :
            lines = int(lines)
            if  1 <= lines <= MAX_LINES :
                break
            else :
                print("Enter a Valid number of lines")
        else :
            print ("Please enter a number")
    return lines

def get_bet() :
    while True : 
        bet = input("How much to do you want to bet on each line : ")
        if bet.isdigit() :
            bet = int(bet)
            if  MIN_BET <= bet <= MAX_BET :
                break
            else :
                print(f"BET Must be between ${MIN_BET}-${MAX_BET}")
        else :
            print ("Please enter a number")
    return bet


def game(balance) :
    lines = get_number_lines()
    while True :
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance :
            print (f"You don't have enough balance to bet on at now . You are balance ${balance}")
        else :
            break
    print (f"You are betting on ${bet} on {lines}.So total bet ${total_bet}")
    slot = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slot)
    wininngs, winnings_line = check_winnings( slot, lines, bet, symbol_value)
    print(f"You won ${wininngs}")
    print(f"You are won on lines: ", *winnings_line)
    
    return wininngs-total_bet



def main() :
    balance = deposit()
    while True : 
        print(f"You'r current balance is ${balance}")
        spin = input("Press enter to play and (q to quit)")
        if (spin=="q") :
            break
        balance += game(balance)


main()