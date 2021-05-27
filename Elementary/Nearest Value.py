"""
Найдите ближайшее значение к переданному.
Вам даны список значений в виде множества (Set) и значение, относительно которого, надо найти ближайшее.
Например, мы имеем следующий ряд чисел: 4, 7, 10, 11, 12, 17. И нам нужно найти ближайшее значение к цифре 9.
Если отсортировать этот ряд по возрастанию, то слева от 9 будет 7, а справа 10.
 Но 10 - находится ближе, чем 7, значит правильный ответ 10.
Несколько уточнений:
Если 2 числа находятся на одинаковом расстоянии - необходимо выбрать наименьшее из них;
Ряд чисел всегда не пустой, т.е. размер >= 1;
Переданное значение может быть в этом ряде, а значит оно и является ответом;
В ряде могут быть как положительные, так и отрицательные числа, но они всегда целые;
Ряд не отсортирован и состоит из уникальных чисел.
Входные данные: Два аргумента. Ряд значений в виде set. Искомое значение - int
Выходные данные: Int.
Пример:
nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
"""


def nearest_value(values: set, one: int) -> int:
    ls_values = sorted(list(values))
    for i in ls_values:
        if one not in ls_values and one < min(ls_values):
            return ls_values[0]
        elif i > one:
            if one - ls_values[ls_values.index(i)-1] <= ls_values[ls_values.index(i)] - one:
                return ls_values[ls_values.index(i)-1]
            else:
                return ls_values[ls_values.index(i)]
        elif one > max(ls_values):
            return ls_values[-1]

#def nearest_value(values: set, one: int) -> int:
    #return sorted(list(values), key=lambda x: (abs(x - one), x))[0]

"""
def nearest_value(values: set, one: int) -> int:
    if one < 0:
        return max(values, key=lambda x: abs(x + one))
    else:
        return min(values, key=lambda x: abs(x - one))
"""


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")