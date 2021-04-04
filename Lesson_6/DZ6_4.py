import re

user_hobby = {}

with open("users.csv", 'r', encoding="utf-8") as f1:
    with open("hobby.csv", 'r', encoding="utf-8") as f2:
          while f1.readline():
            string_fio = " "
            string_hobby = " "
            fio = string_fio.join(re.split(",| *\n", f1.readline()))
            user_hobby[fio] = string_hobby.join(re.split(" *\n", f2.readline()))


print(user_hobby)