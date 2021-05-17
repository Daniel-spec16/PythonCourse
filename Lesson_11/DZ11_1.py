import re


class Data:

    year = 2021

    def __init__(self, string):
        self.string = string

    @classmethod
    def full_date(cls, string):
        string = re.split('/', string)
        day = int(string[0])
        month = int(string[1])
        year = int(string[2])
        return day, month, year

    @staticmethod
    def validation(day, month, year):
        if day > 31 or day < 1:
            raise ValueError
        elif month > 12 or month < 1:
            raise ValueError
        elif year > Data.year:
            raise ValueError

    @staticmethod
    def combine(date_tuple):
        return f"{date_tuple[0]}/{date_tuple[1]}/{date_tuple[2]}"

    def __str__(self):
        return f"Date:{Data.combine(Data.full_date(self.string))}"

    
data_1 = Data("17/09/80")
print(data_1)
