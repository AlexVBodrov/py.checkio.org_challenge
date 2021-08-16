def order(sentence):
    list_num = [x for x in range(1, 10)]
    out_list = []

    sen_list = sentence.split(' ')

    for i in list_num:
        for n in sen_list:
            if i in sen_list:
                out_list.insert(i-1, sen_list[n])
    print(out_list)

    return out_list


print(order("is2 Thi1s T4est 3a")) # === "Thi1s is2 3a T4est"