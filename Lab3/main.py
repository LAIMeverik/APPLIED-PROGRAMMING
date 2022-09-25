alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
encrypt = input("Введите текст: ")
key = int(input("Введите сдвиг: ")) % 33
encrypt = encrypt.lower()
encrypted = " "
decrypted = " "

for latter in encrypt:
    position = alphabet.find(latter)
    newposition = position + key
    if latter in alphabet:
        encrypted = encrypted + alphabet[newposition]
    else:
        encrypted = encrypted + latter
print("Ваш шифр: ", encrypted)

for latter in encrypted:
    position = alphabet.find(latter)
    newposition = position - key
    if latter in alphabet:
        decrypted += alphabet[newposition]
    else:
        decrypted = decrypted + latter
print("Расшифровка: ", decrypted)