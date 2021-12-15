INITIAL_BALANCE = 20
FRUIT_FILE = "fruits.txt"

MAIN_MENU1 = """---------------
欢迎!"""

MAIN_MENU2 = """你可以输入`b`、`l`、`r` 或`e`.
意义如下:
- b: 购买水果
- l: 罗列已购买的
- r: 充值
- e: 退出
请输入命令: """

BALANCE_MENU = "你的余额:"

BUY_MENU1 = "价格如下:"
BUY_MENU2 = "请输入水果名或者首字母: "
BUY_MENU3 = "成功."
BUY_MENU4 = "失败: 余额不足"

LIST_MENU1 = "你已购买: "
RECHARGE_MENU1 = "输入充值金额: "
EXIT_MENU2 = "再见"

INVALID = "输入无效"


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