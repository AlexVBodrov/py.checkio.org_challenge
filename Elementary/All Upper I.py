"""
Проверить все ли символы в строке являются заглавными. Если строка пустая или в ней нет букв - функция должна вернуть True.
Входные данные: Строка.
Выходные данные: Логический тип.
Пример:

is_all_upper('ALL UPPER') == True
is_all_upper('all lower') == False
is_all_upper('mixed UPPER and lower') == False
is_all_upper('') == True
is_all_upper('444') == True
is_all_upper('55 55 5') == True

Условия: a-z, A-Z, 1-9 и пробелы
"""
def is_all_upper(text: str) -> bool:
    if len(text) == 0 or False == ''.join(text.split()).isalpha():
        return True
    else:
        return text.isupper()


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    assert is_all_upper('     ') == True
    assert is_all_upper('444') == True
    assert is_all_upper('55 55 5') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")