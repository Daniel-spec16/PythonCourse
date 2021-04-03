def list_of_bigger_nums(list_num):
    list_big_num = []
    for el in list_num[1:]:
        if el > list_num[list_num.index(el)-1]:
            list_big_num.append(el)

    return list_big_num


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(list_of_bigger_nums(src))


