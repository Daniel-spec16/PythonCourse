class Cell:

    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        new_cell = Cell(self.cells+other.cells)
        return new_cell

    def __sub__(self, other):
        if self.cells > other.cells:
            new_cell = Cell(self.cells - other.cells)
            return new_cell

    def __mul__(self, other):
        new_cell = Cell(self.cells * other.cells)
        return new_cell

    def __truediv__(self, other):
        new_cell = Cell(self.cells // other.cells)
        return new_cell

    def make_order(self, row_num):
        string = ""
        for i in range(self.cells//row_num):
            string += "*"*row_num + "\n"
        string += "*"*(self.cells % row_num)
        return string


cell_1 = Cell(26)
print(cell_1.make_order(5))
