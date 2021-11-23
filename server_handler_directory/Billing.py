

class Billing:
    """The class which represents the bill.
    """
    def __init__(self, date, amount):
        """ Constructs the attributes for a bill

        Args:
            date (string): The date of creating for the bill.
            amount (int): the amount of the money for the bill.
        """        
        self.__date = date
        self.__amount = amount
        self.__ispaid = False

    def __repr__(self):
        """the built in function which defines how the object will be printed

        Returns:
            string: the string representation of the bill object
        """
        return f'Date: {self.__date}, Amount: {self.__amount}, Paid: {self.__ispaid}'

