class IntFloatList:
    @staticmethod
    def check(user_list):
        for el in user_list:
            if type(el) == int:
                pass
            elif type(el) == float:
                pass
            else:
                return "list does not contain only numbers"
        return "List contains only numbers"


list_1 = [19, 28, 2, 4.19]
print(IntFloatList.check(list_1))
