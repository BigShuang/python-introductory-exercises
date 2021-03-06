WELCOME = "Welcome to Sokoban!"
ENTER = "Enter command: "
WIN = "Win!"
BYE = "Bye!"
INVALID = "Invalid command"


DIRECTION = {
    # direction: (dr, dc)
    "w": (-1, 0),
    "a": (0, -1),
    "s": (1, 0),
    "d": (0, 1),
}


def read_txt(filename):
    print(filename)
    with open(filename, "r") as f:
        fr = f.read()

    lines = fr.split("\n")

    board = []
    for line in lines:
        line = line.strip()
        if line:
            board.append(list(line))

    return board


def get_info(board):
    info = {
        "player": [],
        "boxes": [],
    }

    r, c = len(board), len(board[0])

    for ri in range(r):
        for ci in range(c):
            cell = board[ri][ci]
            if cell == "+":
                info["boxes"].append([ri, ci])
                board[ri][ci] = "."
            elif cell == "P":
                info["player"] = [ri, ci]
                board[ri][ci] = "."

    return info


def show_board(board, info):
    r, c = len(board), len(board[0])
    player = tuple(info["player"])
    boxes = info["boxes"]


    for ri in range(r):
        for ci in range(c):
            cell = board[ri][ci]
            if (ri, ci) == player:
                cell = "P"
            elif [ri, ci] in boxes:
                if cell == "-":
                    cell = "O"
                else:
                    cell = "+"

            print(cell, end="")

        print()


def check_win(board, info):
    for box in info["boxes"]:
        br, bc = box
        if board[br][bc] != "-":
            return False

    return True


def move(board, info, drc, step):
    r, c = len(board), len(board[1])
    pr, pc = info["player"]
    dr, dc = drc

    for i in range(step):
        new_r = pr + dr
        new_c = pc + dc
        if board[new_r][new_c] == "#":
            break

        if new_r < 0 or new_r >= r or new_c < 0 or new_c >= c:
            break


        new_rc = [new_r, new_c]
        if new_rc in info["boxes"]:
            index = info["boxes"].index(new_rc)
            next_r, next_c = new_r + dr, new_c + dc
            if board[next_r][next_c] == "#":
                break

            if next_r < 0 or next_r >= r or next_c < 0 or next_c >= c:
                break

            if [next_r, next_c] in info["boxes"]:
                break

            info["boxes"][index] = [next_r, next_c]

        pr = new_r
        pc = new_c

    info["player"] = [pr, pc]


def main(txt_file):
    board = read_txt(txt_file)  # 1. ??????????????????????????????????????????
    info = get_info(board)  # 2. ???????????????????????? ???????????????????????????
    print(WELCOME)  # 3. ???????????????

    # 4. ????????????
    while True:
        # 4-a. ?????????????????????
        show_board(board, info)

        if check_win(board, info):  # 4-b. ??????????????????????????????????????????????????????
            print(WIN)
            return

        cmd = input(ENTER)
        cmd = cmd.lower()
        # 4-d. ??????????????????
        if len(cmd) > 0:
            if cmd[0] == "e":  # 4-e. ??????????????????
                print(BYE)
                return

            # 4-f. ????????????????????????
            direction = cmd[0]
            step = cmd[1:]
            if direction in DIRECTION:
                drc = DIRECTION[direction]
                if step.isdigit():  #
                    # 4-g. ???????????????????????????????????????????????????
                    step = int(step)
                    move(board, info, drc, step)
                    continue

        # 4-h. ???????????????????????????????????????????????????
        print(INVALID)


txt_file = "sokoban.txt"
main(txt_file)