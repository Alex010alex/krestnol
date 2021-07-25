# Alex010alex for Python 3.9
from random import randint
# функция вывода символа в клетку поля
def p(x,y):
    if not((x,y) in field_X):
        if not ((x, y) in field_O):
            return " "
        return "O"
    return "X"
# функция вывода изображения в консоль
def field_to_console():
    print(" |0 1 2|")
    print(" _______")
    print(f"0|{p(0,0)} {p(0,1)} {p(0,2)}|")
    print(f"1|{p(1,0)} {p(1,1)} {p(1,2)}|")
    print(f"2|{p(2,0)} {p(2,1)} {p(2,2)}|")
    print(" -------")
# получает введенные 2 цифры и возвращает код хода
def get_new_move():
    while True:
        str = input("Ход игрока. Введите две цифры - номер строки и столбца (0,1 или 2) и нажмите Ввод")
        position_set = []
        for sss in str:
            if sss == "0" or sss == "1" or sss == "2":
                position_set.append(sss)
                if len(position_set)>1:
                    break
        if len(position_set) > 1:
            return (int(position_set[0]), int(position_set[1]))
        print("Недопустимые символы. Повторите ввод")
# возвращает уникальную позицию введенную игроком
def get_player_choise():
    not_unique_move = True
    while not_unique_move:  # игрок делает уникальный ход
        move = get_new_move()
        if not (move in field_X or move in field_O):
            return move
            not_unique_move = False
        print("Это поле уже занято")
        field_to_console()  # рисуем поле
# возвращает уникальную случайную позицию
def get_computer_choise():
    not_unique_move = True
    while not_unique_move:  # игрок делает уникальный ход
        move = (randint(0, 2),randint(0, 2))
        if not (move in field_X or move in field_O):
            return move
            not_unique_move = False
# функция проверяет есть ли победитель и выводит сообшение и возвращает результат
def is_it_winner():
    win_set = [
        [(0, 0), (1, 1), (2, 2)],
        [(2, 0), (1, 1), (0, 2)],
        [(0, 1), (1, 1), (2, 1)],
        [(1, 0), (1, 1), (1, 2)],
        [(0, 0), (0, 1), (0, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 2), (1, 2), (2, 2)]
    ]
    for www in win_set:
        if set(www).issubset(field_O):
            print("Победа компьютера. Игра окончена.")
            return True
        if set(www).issubset(field_X):
            print("Победа игрока. Поздравления!!!!")
            return True
    return False
# сброс наборов ходов за крестики и нолики
global field_X
global field_O
field_X = set()
field_O = set()
print("Начало игры в крестики-нолики")
print("реализация Alex")
input("To start press a key and Enter")

field_to_console() # рисуем поле
field_X.add(get_player_choise())  # игрок делает ход
# основной цикл
for ttt in range (4):
    field_O.add(get_computer_choise())  # компьютер делает ход
    if is_it_winner():
        break
    field_to_console()  # рисуем поле
    field_X.add(get_player_choise()) # игрок делает ход
    if is_it_winner():
        break
    print(ttt)
    if ttt == 3:
        print('Игра закончена вничью!')
field_to_console()  # рисуем поле
