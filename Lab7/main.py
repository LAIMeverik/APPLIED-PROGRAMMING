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
while True:
    logger.info('Program started')
    # Проверка на ввод и соответствие данных
    try:
        horizontal = int(input('Введите координату клетки фигуры по горизонтали: '))
        if horizontal > 8 or horizontal < 0:
            print('Введены некорректные данные. Попробуйте снова.')
            logger.error('Incorrect value')
            continue
        vertical = int(input('Введите координату клетки фигуры по вертикали: '))
        if vertical > 8 or vertical < 0:
            print('Введены некорректные данные. Попробуйте снова.')
            logger.error('Incorrect value')
            continue
        attackhorizontal = int(input('Введите координату атакуемой клетки по горизонтали: '))
        if attackhorizontal > 8 or attackhorizontal < 0:
            print('Введены некорректные данные. Попробуйте снова.')
            logger.error('Incorrect value')
            continue
        attackvertical = int(input('Введите координату атакуемой клетки по вертикали: '))
        if attackvertical > 8 or attackvertical < 0:
            print('Введены некорректные данные. Попробуйте снова.')
            logger.error('Incorrect value')
            continue
        figure = int(input('''Какую фигуру вы хотите использовать?
        1 -- Ферзь
        2 -- Ладья
        3 -- Слон
        4 -- Конь
        Ваш выбор: '''))
        if figure > 4 or figure < 0:
            print('Введены некорректные данные. Попробуйте снова.')
            logger.error('Incorrect value')
            continue
    except ValueError:
        print('Введены некорректные данные. Попробуйте снова.')
        logger.info('ValueError')
        continue

    # Проверка на совпадение цвета
    if (horizontal + vertical) % 2 == (attackhorizontal + attackvertical) % 2:
        print('Они одного цвета --', end=' ')
        logger.info('Program printed to user')
        if (horizontal + vertical) % 2 == 0:
            print('белого')
        else:
            print('черного')
            logger.info('Program printed to user')
    else:
        print('Нет, они не одного цвета')
        logger.info('Program printed to user')

    # Расстояние по горизонтали и вертикали
    dx = abs(horizontal - attackhorizontal)
    dy = abs(vertical - attackvertical)

    # Проверка угрозы фигуры полю + второй ход
    if figure == 1:     # Ферзь
        if horizontal == attackhorizontal or vertical == attackvertical or dx == dy:
            print(f'Ферзь угрожает полю ({attackhorizontal}; {attackvertical})')
            logger.info('Program printed to user')
        else:
            print(f'Ферзь не угрожает полю ({attackhorizontal}; {attackvertical})')
            print(f'Чтобы за два хода попасть в это поле необходимо встать на поле ({attackhorizontal}; {vertical})')
            logger.info('Program printed to user')
    elif figure == 2:   # Ладья
        if horizontal == attackhorizontal or vertical == attackvertical:
            print(f'Ладья угрожает полю ({attackhorizontal}; {attackvertical})')
            logger.info('Program printed to user')
        else:
            print(f'Ладья не угрожает полю ({attackhorizontal}; {attackvertical})')
            print(f'Чтобы за два хода попасть в это поле необходимо встать на поле ({attackhorizontal}; {vertical})')
            logger.info('Program printed to user')
    elif figure == 3:   # Слон
        if dx == dy:
            print(f'Слон угрожает полю ({attackhorizontal}; {attackvertical})')
            logger.info('Program printed to user')
        else:
            print(f'Слон не угрожает полю ({attackhorizontal}; {attackvertical})')
            if (horizontal + vertical) % 2 != (attackhorizontal + attackvertical) % 2:
                print(f'Слон никаким образом не может угрожать полю ({attackhorizontal}; {attackvertical})')
                logger.info('Program printed to user')
            else:
                attackhorizontal0, attackvertical0, attackhorizontal1, attackvertical1 = attackhorizontal, attackvertical, 0, 0
                while 0 < attackhorizontal0 < 9 and 0 < attackvertical0 < 9:
                    attackhorizontal0 += 1
                    attackvertical0 += 1
                    if abs(horizontal - attackhorizontal0) == abs(vertical - attackvertical0):
                        attackhorizontal1 = attackhorizontal0
                        attackvertical1 = attackvertical0
                        break
                attackhorizontal0 = attackhorizontal
                attackvertical0 = attackvertical
                while 0 < attackhorizontal0 < 9 and 0 < attackvertical0 < 9:
                    attackhorizontal0 += 1
                    attackvertical0 -= 1
                    if abs(horizontal - attackhorizontal0) == abs(vertical - attackvertical0):
                        attackhorizontal1 = attackhorizontal0
                        attackvertical1 = attackvertical0
                        break
                attackhorizontal0 = attackhorizontal
                attackvertical0 = attackvertical
                while 0 < attackhorizontal0 < 9 and 0 < attackvertical0 < 9:
                    attackhorizontal0 -= 1
                    attackvertical0 += 1
                    if abs(horizontal - attackhorizontal0) == abs(vertical - attackvertical0):
                        attackhorizontal1 = attackhorizontal0
                        attackvertical1 = attackvertical0
                        break
                attackhorizontal0 = attackhorizontal
                attackvertical0 = attackvertical
                while 0 < attackhorizontal0 < 9 and 0 < attackvertical0 < 9:
                    attackhorizontal0 -= 1
                    attackvertical0 -= 1
                    if abs(horizontal - attackhorizontal0) == abs(vertical - attackvertical0):
                        attackhorizontal1 = attackhorizontal0
                        attackvertical1 = attackvertical0
                        break
                print(f'Чтобы за два хода попасть в это поле необходимо встать на поле ({attackhorizontal1}; {attackvertical1})')
    else:   # Конь
        if abs(dx - dy) == 1:
            print(f'Конь угрожает полю ({attackhorizontal}; {attackvertical})')
            logger.info('Program printed to user')
        else:
            print(f'Конь не угрожает полю ({attackhorizontal}; {attackvertical})')
            logger.info('Program printed to user')
    break
logger.info('Program done')
