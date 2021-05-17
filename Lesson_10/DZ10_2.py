from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def cloth_waste(self):
        waste = self.size/6.5+0.5
        return waste


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def cloth_waste(self):
        waste = 2*self.height+0.3
        return waste


def total_cloth_waste(*args):
    total = 0
    for el in args:
        total += el.cloth_waste
    return total


suit_1 = Suit(130)
suit_2 = Suit(240)
coat_1 = Coat(13)
coat_2 = Coat(24)
print(suit_1.cloth_waste, suit_2.cloth_waste, coat_1.cloth_waste, coat_2.cloth_waste)
print(total_cloth_waste(suit_1, suit_2, coat_1, coat_2))
