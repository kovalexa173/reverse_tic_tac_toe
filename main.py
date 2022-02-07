from random import choice

board = list(range(1, 101))
free_cells = list(range(1,101))

#генерация матрицы
def generation_matrix(board):
    matrix = [list(board[:10])]
    for i in range(1, 10):
        matrix.append(board[10 * i:10 + 10 * i])
    return matrix
#построение игрового поля
def draw_board(board):
    matrix = generation_matrix(board)
    print("-" * 50)
    for i in range(10):
        for j in range(10):
            if str(matrix[i][j]) == "X":
                print("|", "\033[1;31m X \033[0m", end='')
            elif str(matrix[i][j]) == "O":
                print("|", "\033[32m O \033[0m", end='')
            else:
                print("|", str(matrix[i][j]).ljust(3), end='')
        print()
        print("-" * 50)
    print("\n" * 2)

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
            print("Некорректный ввод. Введите число от 1 до 100 чтобы походить.")


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

    if "X" * 5 in string:
        return "X"

    elif "O" * 5 in string:
        return "O"


#проверка выигрыша
def check_win(board):
    matrix = generation_matrix(board)

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
def main(matrix):
    counter = 0
    win = False
    player = "X"
    computer = "O"

    while not win:
        draw_board(matrix)

        if counter % 2 == 0:
            take_input(player)
        else:
            selection_cell_computer(computer)

        counter += 1

        if counter > 8:
            tmp = check_win(board)

            if tmp == "X":
                draw_board(matrix)
                print("\033[1;31m Компьютер выиграл! \033[0m")
                win = True
                break
            elif tmp == "O":
                draw_board(matrix)
                print("\033[1;31m Вы выиграли! \033[0m")
                win = True
                break

        if counter == 101:
            print("Ничья!")
            break


main(board)


