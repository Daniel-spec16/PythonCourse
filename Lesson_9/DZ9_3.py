class Worker:

   name = "Vasiliy"
   surname = "Vernik"
   position = "Director"
   _income = {"wage": 100000, "bonus": 5}


class Position(Worker):

    def get_full_name(self):
        return self.name+" "+self.surname

    def get_total_income(self):
        return Worker._income["wage"]+Worker._income["bonus"]


position_1 = Position()
print(position_1.get_total_income())