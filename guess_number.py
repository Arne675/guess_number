from random import randint
random_num = randint(1, 100)
while True:
    user_num = int(input('Введите число: '))
    if user_num == random_num:
        print('Отличная интуиция! Вы угадали число :)')
        break;
    elif user_num > random_num:
        print('Ваше число больше того, что загадано')
    else:
        print('Ваше число меньше того, что загадано')