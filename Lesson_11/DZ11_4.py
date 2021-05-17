class Storage:
    places_available = {"A": 500, "B": 500}
    tech_dict = {"A": {}, "B": {}}


    @classmethod
    def add(cls, item, quantity, sector):
        if quantity <= Storage.places_available[sector]:
            Storage.places_available[sector] = Storage.places_available[sector] - quantity
            Storage.tech_dict[sector][item] = quantity


class OrgTech:
    type = "Tech equipment"
    spec = "Office equipment"


class Printer(OrgTech):
    def __init__(self, model, quantity, year):
        self.model = model
        self.quantity = quantity
        self.year = year

    def add_to_storage(self, sector):
        Storage.add(self.model, self.quantity, sector)


Storage.add("printer", 100, "A")
printers = Printer("ZK900", 100, 2014)
printers.add_to_storage("B")
print(Storage.tech_dict)

