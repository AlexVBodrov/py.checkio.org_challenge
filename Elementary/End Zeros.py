"""
Попробуйте выяснить какое количество нулей содержит данное число в конце.
Входные данные: Положительное целое число (int).
Выходные данные: Целое число (int).
Пример:
end_zeros(0) == 1
end_zeros(1) == 0
end_zeros(10) == 1
end_zeros(101) == 0
"""
def end_zeros(num: int) -> int:
    z = str(num)
    count = 0
    if len(z) == 1 and z[0] == '0':
        count = + 1
        return count
    elif len(z) == 1 and z[0] != '0':
        return count
    elif len(z) > 1:
        for i in z[::-1]:
            if i == "0":
                count += 1
            else:
                return count
        return count
    else:
        return 0


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")