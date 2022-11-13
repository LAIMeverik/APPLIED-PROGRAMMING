import logging
import random

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
Данная программа создана для жеребьевки с помощью генерации случайных чисел 
Для того чтобы провести жеребьевку вам необходимо ввести количество(положительное натуральное число) пользователей 
для жеребьевки. 
Далее последствием нажатия клавиши ENTER вам будут выводится соответствующие числа для жеребьевки
''')

while True:
    logger.info('Program started')
    # Ввод данных и проверка на ввод
    try:
        users = int(input('Введите количество пользователей для жеребьевки: '))
    except ValueError:
        print('Данные введены некорректно. Попробуйте снова.')
        logger.error('Incorrect value.')
        continue
    if users <= 0:
        print('Введены некорректные значения. Попробуйте снова.')
        logger.error('Incorrect value.')
        continue
    logger.info(f'User entered value {users}')

    # Создание и заполнение массива чисел от 1 до n
    array = list()
    for i in range(users):
        array.append(i+1)

    # Вывод случайных чисел при помощи удаления уже выпавших
    for i in range(users):
        rand = random.randint(0, len(array) - 1)
        print(array[rand])
        logger.info(f'Displayed number: {array[rand]}')
        array.pop(rand)
        input('Нажмите ENTER для того чтобы вытащить следующее число')

    # Выход из цикла
    break
logger.info('Program done')
