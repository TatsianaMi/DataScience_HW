# Написать программу, которая принимает строку от пользователя и выводит количество символов в этой строке.
# *Дополнительно: считаем отдельно количество пробельных символов
def count_characters_and_spaces(input_string):
    char_count = 0
    space_count = 0

    for char in input_string:
        if char.isspace():
            space_count += 1
        else:
            char_count += 1

    return char_count, space_count

def count_characters(input_string):
    return len(input_string)


if __name__ == "__main__":
    user_input = input("Введите строку: ")
    character_count = count_characters(user_input)
    print(f"Количество символов в строке: {character_count}")
    
    chars, spaces = count_characters_and_spaces(user_input)
    print(f"Количество символов (без пробелов): {chars}")
    print(f"Количество пробелов: {spaces}")



