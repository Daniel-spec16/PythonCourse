import csv
import sys


with open("bakery.csv", "a", encoding="utf-8") as bakery:
        file_writer = csv.writer(bakery, delimiter="\t", lineterminator="\r")

        for arg in sys.argv[1:]:
          file_writer.writerow([sys.argv[1]])

