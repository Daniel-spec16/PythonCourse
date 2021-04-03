src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
#print(set(tuple(src)))
set_src = set(src)
src_sorted = sorted(src)
result = []
for i in set_src:
    if src_sorted[src_sorted.index(i)] != src_sorted[src_sorted.index(i)+1]:
        result.append(i)

#print(*result)
result_end = [el for el in src if el in result]
print(*result_end)



