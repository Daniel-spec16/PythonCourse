class NullDivision:
    @staticmethod
    def divide(nom, denom):
        try:
            return nom/denom
        except ZeroDivisionError:
            return "Division by zero occurred"


div_1 = NullDivision.divide(19, 0)
print(div_1)
