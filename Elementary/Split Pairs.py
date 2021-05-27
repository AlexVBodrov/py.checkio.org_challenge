"""
Разделите строку на пары из двух символов.
Если строка содержит нечетное количество символов,
пропущенный второй символ последней пары должен быть заменен подчеркиванием ('_').
Входные данные: Строка.
Выходные данные: Массив строк.
Пример:
split_pairs('abcd') == ['ab', 'cd']
split_pairs('abc') == ['ab', 'c_']

Предварительное условие: 0<=len(str)<=100
"""

def split_pairs(a):
    # your code here
    out_list = []
    start = 0
    stop = 2
    step = 2
    end = len(a)
    while end > 0:
        out_list.append(a[start: stop])
        start += step
        stop += step
        end -=2
    if len(a) > 0 and len(out_list[-1]) == 1:
        out_list[-1] = out_list[-1] + '_'
    return out_list

"""
def split_pairs(a):
    if len(a) % 2 == 1: a = a + '_'
    return [a[i] + a[i+1] for i in range(0, len(a), 2)]
"""


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")