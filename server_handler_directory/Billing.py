

class Billing:
    """
    A class to represent the billing.
    ...

    Attributes
    ----------
    date : datetime
        the billing date
    amount : int
        the amount of money assigned to the bill
    ispaid : bool
        tells if the bill is paid or not
    """
    def __init__(self, date, amount):
        """
        Constructs the attributes for a bill
        ...
        :param date:
        the creating date for the bill
        :param amount:
        the amount of the money of the bill
        """
        self.__date = date
        self.__amount = amount
        self.__ispaid = False

    def __repr__(self):
        """
        :return:
        a formatted string which contains information of the bill
        """
        return f'Date: {self.__date}, Amount: {self.__amount}, Paid: {self.__ispaid}'

