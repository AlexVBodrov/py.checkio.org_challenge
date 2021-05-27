"""
Вам дана строка, и вы должны найти ее первое слово.
Это упрощенная версия миссии « Первое слово », которую можно будет решить позже.
Входная строка состоит только из английских букв и пробелов.
В начале и в конце строки нет пробелов.
Вход: строка.
Выход: строка.
Предварительное условие: текст может содержать буквы az, AZ и пробелы.
"""

def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    text = text.split()
    return text[0]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!")