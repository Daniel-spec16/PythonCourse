import random

list_of_prices = []
string_of_prices = ","


while len(list_of_prices)!=20:
    list_of_prices.append(round(random.random()*100, 2))

print(f"Generated list of prices: {list_of_prices}")

list_of_prices_copy = list_of_prices.copy()

for el in list_of_prices_copy:
    list_of_prices_copy[list_of_prices_copy.index(el)] = " {0} руб {1} коп".format(str(el).split(".")[0], str(el).split(".")[1])

print(f'Simple string of prices: {string_of_prices.join(list_of_prices_copy)}')


list_of_prices = sorted(list_of_prices)
print(f'Цены по возрастанию: {list_of_prices}')
list_of_prices_downgrade = list_of_prices.copy()
list_of_prices_downgrade.reverse()
print(f'Цены по убыванию: {list_of_prices_downgrade}')
print(f'5 самых дорогих товаров: {list_of_prices[-5:]}')





