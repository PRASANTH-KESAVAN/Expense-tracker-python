from expense import Expense
import calendar
import datetime


def main():
    budget = 100000
    expense_file_path = "expenses.csv"
    # get the expense
    expense = get_expense()
    print(yellow(expense))

    # write the expense into a file

    write_expense(expense, expense_file_path)

    # read it and summarize it
    summarize(expense_file_path, budget)

    pass


def get_expense():
    expense_name = input("Enter the expense name: ")
    expense_amount = float(input("Enter the amount:$"))

    category = [
        "Food",
        "Home",
        "work",
        "Fun"

    ]

    # It executes the loop until user enter a valid input
    while True:
        print(radiant_cyan(f"Select the expense category: "))
        for i, category_name in enumerate(category):
            print(purple(f"{i + 1}. {category_name} "))  # i+1 helps to start the index from 1

        category_length = len(category)
        # Since the index starts from 0 but category starts from 1 we are reducing 1 number to fet correct index number
        selected_index = int(input(f"Enter the category number between {1}-{category_length}: ")) - 1

        if selected_index in range(category_length):
            selected_category = category[selected_index]

            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense

        else:
            print("Invalid category")


def write_expense(expense, expense_file_path):
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarize(expense_file_path, budget):
    expenses = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()  # read each lines from the file

        for line in lines:
            # print(line)
            expense_name, expense_amount, expense_category = line.strip().split(
                ",")  # removes blankspace and separeate them by ','

            new_expense = Expense(name=expense_name, category=expense_category, amount=float(expense_amount))
            expenses.append(new_expense)  # saves objects to expenses file

    amount_category = {}

    # here expense is a object so acces it using '.'
    for expense in expenses:
        key = expense.category
        if key in amount_category:
            amount_category[key] += expense.amount

        else:
            amount_category[key] = expense.amount

    print(radiant_cyan("Expense by category:"))
    for key, value in amount_category.items():
        print(blue(f"{key}: ${value}"))

    amount_spent = sum([x.amount for x in expenses])

    remaining_amount = budget - amount_spent
    print(f"Remaing amount:${remaining_amount}")

    if remaining_amount < 0:
        print(red(f"Unfortunately, there is no budget available "))
    else:
        now = datetime.datetime.now()
        days_in_month = calendar.monthrange(now.year, now.month)[1]
        remaining_days = days_in_month - now.day

        daily_budget = remaining_amount / remaining_days
        print(green(f"Budget per day:${daily_budget}"))


def red(text):
    return f"\033[91m{text}\033[0m"


def green(text):
    return f"\033[92m{text}\033[0m"

def yellow(text):
    return f"\033[93m{text}\033[0m"

def radiant_cyan(text):
    return f"\033[96m{text}\033[0m"

def purple(text):
    return f"\033[95m{text}\033[0m"

def blue(text):
    return f"\033[94m{text}\033[0m"


# it helps to run full code whwn it run from this file directly
# if any function from this file is imported to another file it will not run the full code
if __name__ == "__main__":
    main()
