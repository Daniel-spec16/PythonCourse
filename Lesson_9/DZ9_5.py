class Stationery:
    title = ""

    def draw(self):
        return "Запуск Отрисовки"


class Pen(Stationery):
    def __init__(self, title=None):
        self.title = title

    def draw(self):
        return "Drawing smthing!"


class Pencil(Stationery):
    def __init__(self, title=None):
        self.title = title

    def draw(self):
        return "item #1 for John Wick"


class Handle(Stationery):
    def __init__(self, title=None):
        self.title = title

    def draw(self):
        return "Handling operation"