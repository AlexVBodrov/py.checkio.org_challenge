"""
В этой задаче, Вам нужно создать функцию проверки пароля.
Условия проверки:
длина пароля должна быть больше 6.
Входные данные: Строка.
Выходные данные: Логический тип.
Пример:
is_acceptable_password('short') == False
is_acceptable_password('muchlonger') == True
1
2
Для чего это нужно: Для проверки заполнения пароля. Кроме того, полезно будет научиться оценивать задачи.
"""
def is_acceptable_password(password: str) -> bool:
    if len(password) > 6:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")