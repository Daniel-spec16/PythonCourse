def odd_nums(n):
    return (el for el in range(1, n+1, 2))


x = odd_nums(15)
print(next(x))
print(next(x))
print(list(x))
