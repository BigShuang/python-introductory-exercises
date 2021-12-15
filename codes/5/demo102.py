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
    # 读取文本文件，得到价格信息
    return {}


def buy_fruit(fruit_prices, balance, bought):
    # 尝试购买水果，购买成功则扣费，不成功不扣费
    # 返回新的余额
    return balance


def list_bought(bought):
    # 罗列已购买的水果信息
    pass


def recharge(balance):
    # 充值，返回新的余额
    return balance


def main(fruit_file, balance):
    # 主函数，展示主菜单与处理主要命令
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