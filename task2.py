# 2.	Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

from random import *

candies = 2021
user_name_1 = input('Input name of first player: ')
user_name_2 = input('Input name of second player: ')
step = bool(randint(0, 2))
while candies > 0:
    print('Remains candies: ', candies)
    if step:
        step_total = int(input('First player steps: '))
        if step_total > 28:
            while step_total > 28:
                print('Enter correct number of candies')
                step_total = int(input('First player steps: '))
                candies -= step_total
                step = not step
        else:
            candies -= step_total           
            step = not step
    else:
        step_total = int(input('Second player', user_name_2, 'steps: '))
        if step_total > 28:
            while step_total > 28:
                print('Enter correct number of candies')
                step_total = int(input('Second player steps: '))    
                candies -= step_total
                step = not step
        else:
            candies -= step_total
            step = not step

if step:
    print(user_name_2 +  'win!!!')
else:
    print(user_name_1 +  'win!!!')