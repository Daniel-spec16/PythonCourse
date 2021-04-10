import os
import sys

directory = sys.argv[1]
print(os.listdir(directory))


def files_bytes_stats(directory):
    less_100 = 0
    less_1000 = 0
    less_10000 = 0
    less_100000 = 0
    dict_of_values = {}
    for file in os.scandir(directory):
        if os.stat(file).st_size < 100:
            less_100 += 1
        elif os.stat(file).st_size < 1000 and os.stat(file).st_size > 100:
            less_1000 += 1
        elif os.stat(file).st_size < 10000 and os.stat(file).st_size > 1000:
            less_10000 += 1
        elif os.stat(file).st_size < 100000 and os.stat(file).st_size > 10000:
            less_100000 += 1
    dict_of_values[100] = less_100
    dict_of_values[1000] = less_1000
    dict_of_values[10000] = less_10000
    dict_of_values[100000] = less_100000
    return dict_of_values


print(files_bytes_stats(directory))