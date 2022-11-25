print('''Доброго времени суток, дорогие пользователи.
Данная программа создана для шифрования методом Цезаря
Для того чтобы зашифровать сообщение введите сообщение и сдвиг шифра.  
''')
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
#Запрашиваем на вход строку текста и сдвиг шифра
encrypt = input("Введите текст: ")
key = int(input("Введите сдвиг: ")) % 33
#переводим строку в прописные буквы
encrypt = encrypt.lower()
encrypted = " "
decrypted = " "

for latter in encrypt:
    #Ищем букву в Алфавите и если она найдена, меняем ее по сдвигу
    position = alphabet.find(latter)
    newposition = position + key
    if latter in alphabet:
        encrypted = encrypted + alphabet[newposition]
    else:
        encrypted = encrypted + latter
#Выводим зашифрованную строку
print("Ваш шифр: ", encrypted)

for latter in encrypted:
    # Ищем букву в Алфавите и если она найдена, меняем ее по сдвигу обратно
    position = alphabet.find(latter)
    newposition = position - key
    if latter in alphabet:
        decrypted += alphabet[newposition]
    else:
        decrypted = decrypted + latter
#Выводим зашифрованную строку
print("Расшифровка: ", decrypted)