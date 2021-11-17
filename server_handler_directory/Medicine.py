
class Medicine:
    def __init__(self, name, dosis, amount, price):
        self.__name = name
        self.__dosis = dosis
        self.__amount = amount
        self.__price = price
        self.__filled = False
        self.__added_to_bill = False


    def mark_as_filled(self):
        self.__filled = True

    def mark_as_billed(self):
        self.__added_to_bill = True

    def __repr__(self):
        return self.__name

    def __eq__(self, other):
        if self.__name == other.__name and self.__price == other.__price \
                and self.__dosis == other.__dosis and self.__amount == other.__amount:
            return True
        return False


