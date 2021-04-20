class Matrix:
    def __init__(self, args):
        self.first_line = args[0]
        self.second_line = args[1]
        self.third_line = args[2]

    def compose(self):
        if len(self.first_line) == len(self.second_line) and len(self.first_line) != len(self.third_line):
            print(self.first_line)
            print(self.second_line)
        elif len(self.first_line) == len(self.second_line) and len(self.second_line) == len(self.third_line):
            print(self.first_line)
            print(self.second_line)
            print(self.third_line)


matrix_1 = Matrix([[0, 7, 9], [7, 13, 6], [19, 18, 17], "sdfhsph"])
matrix_1.compose()
