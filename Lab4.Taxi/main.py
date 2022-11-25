print('''Доброго времени суток, дорогие пользователи.
Данная программа создана для выгодного и быстрого распледеления такси для отвоза сотрудников домой.
Введите количество сотрудников, расстояние до дома и тариф за 1 км в рублях.  
''')
import num2t4ru

#Создаем словари в которых будет информация о расстоянии, стоимости, и сотрудников.
employees = dict()
cars = dict()
answers = dict()
#Создаем листы с ответом по сотрудникам и машинам
lemployees = list()
lcars = list()

sum = 0

male_units = ((u'рубль', u'рубля', u'рублей'), 'm')

count = int(input("Введите количество сотрудников: "))
#Вводим информацию о расстояниях до домов сотрудников
for i in range(1, count + 1):
    employees[i] = int(input("Введите растояние до дома сотрудника №" + str(i) + ": "))
#Вводим информацию о тарифах на машины
for i in range(1, count + 1):
    cars[i] = int(input("Введите тариф за 1км для машины №" + str(i) + ": "))
#Сортируем сотрудников по их расстояниям
sorted_tuple = sorted(employees.items(), key=lambda x: x[1])
employees = dict(sorted_tuple)
#Сортируем такси по стоимостям тарифов
sorted_tuple = sorted(cars.items(), reverse=True, key=lambda x: x[1])
cars = dict(sorted_tuple)
#Объединяем сотрудников и машины в листах
for key in employees.keys():
    lemployees.append(key)

for key in cars.keys():
    lcars.append(key)
#Вносим информацию в конечный словарь
for i in range(0, count):
    answers[i] = [lemployees[i], lcars[i]]
#Подсчитываем итоговую сумму
for answer in answers.items():
    sum += employees[answer[1][0]] * cars[answer[1][1]]
    print(answer[1][1])
#Выводим ответ с суммой
print(
    "Стоимость развоза всех сотрудников составила - " + str(sum) + " руб. (" + num2t4ru.num2text(sum, male_units) + ")")
