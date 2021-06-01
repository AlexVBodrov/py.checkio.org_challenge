"""
Отсортируйте данный итератор таким образом,
чтобы его элементы оказались в порядке убывания частоты их появления,
то есть по количеству раз, которое они появляются в элементах.
Если два элемента имеют одинаковую частоту, они должны оказаться в том же порядке, в котором стояли изначально в итераторе.
Входные данные: Итератор
Выходные данные: Итератор
Пример:
frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) == ['bob', 'bob', 'bob', 'carl', 'alex']
Предварительное условие: Элементы могут быть целыми числами или строками.
Миссия была взята из Python CCPS 109 Осень 2018.
"""

def listmerge3(lstlst):
    all=[]
    for lst in lstlst:
      all.extend(lst)
    return all

def frequency_sort(items):
    if len(items) == 0:
        return items
    out_ls = []
    new_ls = []
    dic_frec = {i: items.count(i) for i in items}
    sorted_tuples = sorted(dic_frec.items(), key=lambda item: item[1], reverse=True)
    sorted_dict = {k: v for k, v in sorted_tuples}
    a = list(map(list, sorted_dict.items()))
    for i in a:
        out_ls.append((str(i[0])+' ') * i[1])
    for i in out_ls:
        new_ls.append(i.split(' '))
    out_ls = listmerge3(new_ls)
    out_ls = list(filter(lambda a: a != '', out_ls))
    if out_ls[0].isdigit():
            out_ls = list(map(int, out_ls))
    return out_ls

"""
def frequency_sort(items):
    #Just return the items array, sorted by count, then by index.
    #Because of the reverse sort, one should add a minus sign
    #in front of the index parameter
    return sorted(items,key=lambda n:(items.count(n),-items.index(n)),reverse=True)
"""
"""
def frequency_sort(items):
    count = {}
    unique_items = []
    for item in items:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
            unique_items.append(item)
    items = []
    for item in sorted(unique_items, key=lambda x: -count[x]):
        items.extend([item] * count[item])
    return items
"""

if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    assert list(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 2, 2, 2, 6, 6]
    print("Coding complete? Click 'Check' to earn cool rewards!")