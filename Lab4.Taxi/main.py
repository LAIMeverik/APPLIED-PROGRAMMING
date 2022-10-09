import num2t4ru

employees = dict()
cars = dict()
answers = dict()

lemployees = list()
lcars = list()

sum = 0

male_units = ((u'рубль', u'рубля', u'рублей'), 'm')

count = int(input("Введите количество сотрудников: "))

for i in range(1, count + 1):
    employees[i] = int(input("Введите растояние до дома сотрудника №" + str(i) + ": "))

for i in range(1, count + 1):
    cars[i] = int(input("Введите тариф за 1км для машины №" + str(i) + ": "))

sorted_tuple = sorted(employees.items(), key=lambda x: x[1])
employees = dict(sorted_tuple)

sorted_tuple = sorted(cars.items(), reverse=True, key=lambda x: x[1])
cars = dict(sorted_tuple)

for key in employees.keys():
    lemployees.append(key)

for key in cars.keys():
    lcars.append(key)

for i in range(0, count):
    answers[i] = [lemployees[i], lcars[i]]

for answer in answers.items():
    sum += employees[answer[1][0]] * cars[answer[1][1]]
    print(answer[1][1])

print(
    "Стоимость развоза всех сотрудников составила - " + str(sum) + " руб. (" + num2t4ru.num2text(sum, male_units) + ")")
