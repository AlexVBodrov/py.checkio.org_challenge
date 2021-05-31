"""
Дан непустой массив целых чисел (X). В этой задаче вам нужно вернуть массив, состоящий только из неуникальных элементов данного массива. Для этого необходимо удалить все уникальные элементы (которые присутствуют в данном массиве только один раз). Для решения этой задачи не меняйте оригинальный порядок элементов. Пример: [1, 2, 3, 1, 3], где 1 и 3 неуникальные элементы и результат будет [1, 3, 1, 3].
non-unique-elements
Вх. данные: Список (list) целых чисел (int).
Вых. данные: Итератор (an iterable) целых чисел (int).
Пример:
checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
checkio([1, 2, 3, 4, 5]) == []
checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]
Как это используется: Эта задача поможет вам понять, как манипулировать массивами.
Это полезный базис для решения более сложных задач.
Также эта идея может быть легко обобщена для реальных задач.
Для примера: если вам необходимо очистить статистику от редко встречающихся элементов (шум).
Предусловия:
0 < len(data) < 1000
"""
def checkio(data: list) -> list:
    new_ls = []
    for i in data:
        if data.count(i)>1:
            new_ls.append(i)
    return new_ls

    #return [x for x in data if data.count(x)>1]

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")