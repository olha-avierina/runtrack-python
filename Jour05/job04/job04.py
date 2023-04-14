def shift_message(message, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # Создаем строку с алфавитом
    shifted_message = ''  # Создаем пустую строку для хранения сдвинутого сообщения

    for char in message:
        if char.lower() in alphabet:  # Проверяем, является ли символ буквой из алфавита
            is_uppercase = char.isupper()  # Проверяем, является ли символ заглавной буквой
            char = char.lower()  # Приводим символ к нижнему регистру для обработки

            # Вычисляем индекс символа в алфавите
            old_index = alphabet.index(char)
            # Вычисляем новый индекс символа с учетом сдвига
            new_index = (old_index + shift) % 26
            # Получаем символ с новым индексом из алфавита
            new_char = alphabet[new_index]

            if is_uppercase:  # Если исходный символ был заглавной буквой
                new_char = new_char.upper()  # Приводим новый символ к заглавной букве

            shifted_message += new_char  # Добавляем новый символ к сдвинутому сообщению
        else:
            # Если символ не является буквой из алфавита, добавляем его без изменений
            shifted_message += char

    return shifted_message  # Возвращаем сдвинутое сообщение


massage: "Bonjour"
shift: 3
shifted_message
