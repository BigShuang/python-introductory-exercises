INITIAL_BALANCE = 20
FRUIT_FILE = "fruits.txt"

MAIN_MENU1 = """---------------
Welcome!"""

MAIN_MENU2 = """You can enter `b`, `l`, `r` or `e`.
The meaning is as follows:
- b: buy fruit
- l: list fruits you have bought
- r: recharge
- e: exit
Enter your command: """

BALANCE_MENU = "Your balance left:"

BUY_MENU1 = "Prices are as follows:"
BUY_MENU2 = "Please enter the fruit name or first letter: "
BUY_MENU3 = "Successfully."
BUY_MENU4 = "Failed: insufficient balance"

LIST_MENU1 = "You have bought: "
RECHARGE_MENU1 = "Enter recharge num: "
EXIT_MENU2 = "Bye"

INVALID = "Invalid Input."


def read_fruit_price(fruit_file):
    fruit_price = {}

    with open(fruit_file, 'r') as f:
        fr = f.read()

    lines = fr.split("\n")
    for line in lines:
        line = line.strip()
        if line:
            fruit, price = line.split(",")
            price = int(price)
            fruit_price[fruit] = price

    return fruit_price


def buy_fruit(fruit_prices, balance, bought):
    while True:
        print(BUY_MENU1)
        for fruit in fruit_prices:
            print("{:<10s}: {}".format(fruit, fruit_prices[fruit]))

        choice = input(BUY_MENU2)

        if len(choice) == 1:
            for fruit in fruit_prices:
                if fruit.startswith(choice):
                    choice = fruit
                    break

        if choice in fruit_prices:
            price = fruit_prices[choice]
            if balance >= price:
                bought.append(choice)
                balance -= price
                print(BUY_MENU3)
            else:
                print(BUY_MENU4)

            return balance

        print(INVALID)


def list_bought(bought):
    print(LIST_MENU1)
    print("    ", end="")

    for fruit in bought:
        print(fruit, end=", ")

    print()


def recharge(balance):
    while True:
        num = input(RECHARGE_MENU1)
        if num.isdigit():
            num = int(num)
            return balance + num
        else:
            print(INVALID)


def main(fruit_file, balance):
    fruit_price = read_fruit_price(fruit_file)
    bought = []
    balance = balance

    while True:
        print(MAIN_MENU1)
        print(BALANCE_MENU, balance)
        cmd = input(MAIN_MENU2)
        if cmd == "b":
            balance = buy_fruit(fruit_price, balance, bought)
        elif cmd == "l":
            list_bought(bought)
        elif cmd == "r":
            balance = recharge(balance)
        elif cmd == "e":
            print(BALANCE_MENU, balance)
            list_bought(bought)
            print(EXIT_MENU2)
            break
        else:
            print(INVALID)


main(FRUIT_FILE, INITIAL_BALANCE)