#3.	Создайте программу для игры в ""Крестики-нолики"".

playing_area = list(range(1, 10))
winning_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (7, 5, 3), (9, 5, 1), (7, 4, 1), (8, 5, 2), (9, 6, 3)]

def create_playing_area ():
    print('------------------')
    for i in range(3):
        print('|', playing_area[0 + i*3], '|', playing_area[1 + i*3], '|', playing_area[2 + i*3], '|')
    print('------------------')

def take_enter(step):
    while True:
        meaning = input('Where do you want to put it: '+ step + '?: ')
        if not (meaning in '123456789'):
            print('Try again.')
            continue
        meaning = int(meaning)
        if str(playing_area[meaning - 1]) in 'xo':
            print('The cell is occupied.')
            continue
        playing_area[meaning - 1] = step
        break

def check_winning_combinations ():
    for each in winning_combinations:
        if (playing_area[each[0] - 1] == playing_area[each[1] - 1] == playing_area[each[2] - 1]):
            return playing_area[each[1] - 1]
    else:
        return False

def main():
    total = 0
    while True:
        create_playing_area()
        if total%2 == 0:
            take_enter('X')
        else:
            take_enter('O')
        if total > 3:
            winner = check_winning_combinations()
            if winner:
                create_playing_area()
                print(winner + ' win!!!')
                break
        total += 1
        if total > 8:
            create_playing_area()
            print('No winner found :C')
            break

main()
