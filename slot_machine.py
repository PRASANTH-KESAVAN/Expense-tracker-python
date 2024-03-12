MAX_LINES = 3
MIN_LINES = 1
MIN_BET = 1
MAX_BET = 1000


# this function helps to deposit the money
def deposit():
    # While goes on until the user enter the valid number
    while True:
        a = input("Enter the amount to deposit: $")

        # helps to make sure the number is digit
        if a.isdigit():
            balance = int(a)
            if balance > 0:  # Entered amount must be greater than zero
                # print(f"Balance :{balance}")
                break

            else:
                print("Number must be greater than zero.")

        else:
            print("Number is not valid ")

    return balance


# to get the number of bets
def get_lines():
    while True:
        lines = input(f"Enter the number of lines between {MIN_LINES}-{MAX_LINES}:")
        if lines.isdigit():
            lines = int(lines)

            if MIN_LINES <= lines <= MAX_LINES:
                break

            else:
                print(f"Choose lines between {MIN_LINES}-{MAX_LINES}.")

        else:
            print("Enter a valid number.")

    return lines


# to get the bets on each line
def get_bets():
    while True:
        bets = input(f"Enter the bets for each line between {MIN_BET}-{MAX_BET}:$")
        if bets.isdigit():
            bets = int(bets)

            if MIN_BET <= bets <= MAX_BET:
                break

            else:
                print(f"Choose bets between {MIN_BET}-{MAX_BET}.")

        else:
            print("Enter a valid number.")

    return bets


# Driver code
def main():
    balance = deposit()  # balance keeps track of deposited money
    lines = get_lines()  # gets the number of lines(bets)

    while True:
        bet = get_bets()  # gets bet for each line
        total_bets = bet * lines

        print(f"\nAvailable balance {balance}")
        print(f"\nNumber of bets = {lines}")

        if balance < total_bets:
            print(f"There is no enough balance, Available balance ${balance}")

        else:
            print(f"\nBets on each line: ${bet}")
            print(f"\nTotal bets: ${total_bets}")
            break


main()
