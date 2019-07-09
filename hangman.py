# !/usr/bin/env python3

import random


def hangman():
    word_list = ['вирус', 'программа', 'компьютер', 'хакер', 'взлом']
    random_number = random.randint(0, 4)
    word = word_list[random_number]
    wrong = 0
    stages = ["", "________      ", "|      |      ", "|      0      ", "|     /|\     ", "|     / \     ", "|"]
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print('Добро пожаловать на казнь!')

    while wrong < len(stages)-1:
        print('\n')
        msg = 'Введіть букву: '
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((' '.join(board)))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('Ви виграли. Загаданим словом було: ')
            print(' '.join(board))
            win = True
            break
        
    if not win:
        print('\n'.join(stages[0:wrong]))
        print('Ви програли! Загадиним словом було: {}'.format(word))
            
    
hangman()
