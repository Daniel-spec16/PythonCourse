import csv
import sys


with open("bakery.csv", "r", encoding="utf-8") as bakery:
        file_reader = csv.reader(bakery, delimiter=" ")
        rows = list(file_reader)
        try:
          if len(sys.argv)==1:
              row_num=0
              while row_num!=len(rows):
                  print(*rows[row_num])
                  row_num += 1
          else:
              begin = sys.argv[1]
              end = sys.argv[2]
              while int(begin)!= end:
                  print(*rows[int(begin)-1])
                  begin = int(begin)+1


        except IndexError:
            try:
              while True:
                print(*rows[int(begin)-1])
                begin = int(begin) + 1
            except IndexError:
                pass

