

class Billing:
    def __init__(self, date, amount):
        self.__date = date
        self.__amount = amount
        self.__ispaid = False

    def __repr__(self):
        return f'Date: {self.__date}, Amount: {self.__amount}, Paid: {self.__ispaid}'

