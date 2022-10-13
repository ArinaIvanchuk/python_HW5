#a) Добавьте игру против бота
from random import *

candies = 2021
user_name_1 = input('Input name of first player: ')
user_name_2 = 'bot'
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
        step_total = randint(1, 29)
        if candies < 28:
           step_total = randint(1, candies)
           print(f'Step bot: {step_total}')
           candies -= step_total
           step = not step
        else:
            print(f'Step bot: {step_total}') 
            candies -= step_total
            step = not step

if step:
    print(user_name_2 +  'win!!!')
else:
    print(user_name_1 +  'win!!!')