from random import choice

board = list(range(1,101))
free_cells = list(range(1,101))


#построение игрового поля
def draw_board(board):
    print("-" * 47)
    print(*board[:10], sep="  | ")
    print("-" * 47)

    for i in range(1,10):
        print(*board[10 * i:10 + 10*i], sep=" | ")
        print("-" * 47)


#функция выбора игровой роли человека: крестик или нолик
def player_choice():
    player_first = ""

    while player_first not in ('X', 'O'):
        player_first = input('Вы хотите играть за X или O? ').upper()

    return player_first


#выбор ячейки для игрока
def take_input(player_token):
    valid = False

    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")

        try:
            player_answer = int(player_answer)

        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue

        if player_answer >= 1 and player_answer <= 100:

            if board[player_answer-1] in free_cells:
                board[player_answer-1] = player_token
                free_cells.remove(player_answer)
                valid = True

            else:
                print("Эта клеточка уже занята")

        else:
            print("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")


#выбор ячейки для компьютера
def selection_cell_computer(computer_token):
    computer_answer = choice(free_cells)
    board[computer_answer - 1] = computer_token
    free_cells.remove(computer_answer)

#функция прверки вхождения "ХО" в строку
def check_entry(arr):
    string = ""

    for j in arr:
        string += str(j)

    if "X " * 5 in string:
        return "O"

    elif "O " * 5 in string:
        return "X"


#проверка выигрыша
def check_win(board):
    matrix = [board[0:10]]

    for i in range(1, 10):
        matrix.append(board[10 * i:10 + 10 * i])

    #проверка горизонталей
    for i in matrix:
        win = check_entry(i)
        if win:
            return win

    #проверка вертикалей
    for i in range(10):
        arr = []
        for j in range(10):
            arr.append(matrix[j][i])
        win = check_entry(arr)
        if win:
            return win

    #проверка диагоналей
    fdiag = [[] for i in range(20 - 1)]
    bdiag = [[] for i in range(len(fdiag))]
    min_bdiag = -10 + 1

    for y in range(10):
        for x in range(10):
            fdiag[x + y].append(matrix[y][x])
            bdiag[-min_bdiag + x - y].append(matrix[y][x])

    for i in fdiag:
        win = check_entry(i)
        if win:
            return win

    for i in bdiag:
        win = check_entry(i)
        if win:
            return win

    return False


#основная функция игры
def main(board):
    counter = 0
    win = False
    player = player_choice()

    if player == "X":
        player = "X "
        computer = "O "
    else:
        computer = "X "

    while not win:
        draw_board(board)

        if counter % 2 == 0:
            take_input(player)
        else:
            selection_cell_computer(computer)

        counter += 1

        if counter > 8:
            tmp = check_win(board)

            if tmp:
                print(tmp, "выиграл!")
                win = True
                break

        if counter == 101:
            print("Ничья!")
            break

    draw_board(board)

main(board)


