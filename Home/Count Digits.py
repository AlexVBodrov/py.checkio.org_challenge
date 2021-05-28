"""
Вам нужно посчитать количество цифр в данной строке.
Вход: ул.
Выход: Int.
Пример:
count_digits ( 'привет' ) == 0
count_digits ( 'кто здесь 1-й' ) == 1
count_digits ( 'мои числа 2' ) == 1
count_digits ( 'Эта картина - холст, масло'
 'картина датской художницы Анны'
 'Петерсен между 1845 и 1910 годом' ) == 8
count_digits ( '5 плюс 6 равно' ) == 2
count_digits ( '' ) == 0
"""

def count_digits(text: str) -> int:
    # your code here
    count =0
    for i in text:
        if i.isdigit():
            count +=1
    return count

    #return sum(c.isdigit() for c in text)

if __name__ == '__main__':
    print("Example:")
    print(count_digits('hi'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_digits('hi') == 0
    assert count_digits('who is 1st here') == 1
    assert count_digits('my numbers is 2') == 1
    assert count_digits('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 8
    assert count_digits('5 plus 6 is') == 2
    assert count_digits('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")