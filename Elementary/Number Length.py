"""
Вам дано положительное целое число. Определите сколько цифр оно имеет.
Входные данные: Положительное целое число
Выходные данные: Целое число.
Пример:
number_length(10) == 2
number_length(0) == 1
"""
def number_length(a: int) -> int:
    l = int(len(str(a)))
    return l


if __name__ == '__main__':
    print("Example:")
    print(number_length(10))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert number_length(10) == 2
    assert number_length(0) == 1
    assert number_length(4) == 1
    assert number_length(44) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")