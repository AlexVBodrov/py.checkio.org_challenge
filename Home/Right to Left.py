"""
Один робот был занят простой задачей: объединить последовательность строк
 в одно выражение для создания инструкции по обходу корабля.
 Но робот был левша и зачастую шутил и запутывал своих друзей правшей.
Дана последовательность строк. Вы должны объединить эти строки в блок текста,
разделив изначальные строки запятыми. В качестве шутки над праворукими роботами,
вы должны заменить все вхождения слова "right" на слова "left", даже если это часть другого слова.
Все строки даны в нижнем регистре.
Входные данные: Последовательность строк.
Выходные данные: Текст, как строка.
Пример:
left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
left_join(("bright aright", "ok")) == "bleft aleft,ok"
left_join(("brightness wright",)) == "bleftness wleft"
left_join(("enough", "jokes")) == "enough,jokes"
Как это используется: Это просто пример операций, использующих строки и последовательности.
Предусловие:
0 < len(phrases) < 42
"""


def left_join(phrases: tuple) -> str:
    """
        Join strings and replace "right" to "left"
    """
    edited_i = [i.replace("right", "left") for i in phrases]
    myString = ','.join(edited_i)
    return myString
    #return (",".join(phrases)).replace("right","left")
#left_join=lambda p:",".join(p).replace("right","left")

if __name__ == '__main__':
    print('Example:')
    print(left_join(("left", "right", "left", "stop")))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
