import num2t4ru

amount_payable = int(input("Введите число: "))

male_units = ((u'рубль', u'рубля', u'рублей'), 'm')

print(num2t4ru.num2text(amount_payable, male_units))
