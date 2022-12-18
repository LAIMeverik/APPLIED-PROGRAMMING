from random import random
import logging

# Работа с логированием
logger = logging.getLogger("Logger")
logger.setLevel(logging.INFO)

# Создан файл для логирования
file_handler = logging.FileHandler("log.log")
# Создание форматера отображающего дату, время, имя логгера, уровень и сообщение
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Диалог с пользователем
print('''Доброго времени суток, дорогие пользователи.
Данная программа загадывает число, которое пользователю необходимо угадать.
Для того чтобы загадать число вам необходимо ввести максимальное число,которое может загадать компьютер и количество(положительное натуральное число) попыток.''')

def gg(n, k):
    f = round(random() * n)
    i = 0
    # Цикл, сравнивающий введенное значение с загаданным
    while i < k:
        logger.info('Program started')
        g = int(input('Впишите число: '))
        if g <= 0:
            print('Ваше число меньше заданного предела. Заданный предел от 1 до', n, 'включительно')
            logger.error('Incorrect value.')
        if g > n:
            print('Ваше число больше заданного предела. Заданный предел от 1 до', n, 'включительно')
        if g == f:
            return print('Вы угадали!')
        else:
            if g < f:
                print('Загаданное число больше')
            else:
                print('Загаданное число меньше')
        # Счетчик попыток
        i += 1
        print('Кол-во оставшихся попыток: ', k - i)

    return print('У вас закончились попытки')

# Данные, введенные пользователем
n = int(input('Максимальное число, которое может быть загадано: '))
k = int(input('Количество попыток: '))
gg(n, k)
logger.info('Program done')