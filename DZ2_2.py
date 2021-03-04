# Это задача 3
# Алгоритм в цикле отвечает на вопрос 4 задачи по поиску чисел в списке даже со знаком
string_of_items = " "
list_of_items = ['в', '05', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for el in list_of_items:
    z = [char for char in el]
    try:
       int(z[len(z)-1])
       list_of_items[list_of_items.index(el)] = str('"{}"'.format(el))
       print(list_of_items[list_of_items.index(el)])

    except ValueError:
        pass
print(string_of_items.join(list_of_items))


