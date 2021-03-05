array = [i**3 for i in range(1001)]
print(array)
sum_of_seven = 0


for j in array:
   split_number = list(map(int, str(j)))

   if sum(split_number)%7==0:
       sum_of_seven += j

print(sum_of_seven)

for j in array:
    if j !=0:
     j += 17
     split_number = list(map(int, str(j)))

     if sum(split_number) % 7 == 0:
        sum_of_seven += j

print(sum_of_seven)
