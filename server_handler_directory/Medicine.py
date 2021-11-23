
class Medicine:
    """Object to represent medicine.
    """    
    def __init__(self, name, dosis, amount, price):
        """ Constructs all the necessary attributes for the Medicine object.

        Args:
            name (string): Name of the medicine.
            dosis (string): Dosis of the medicine.
            amount (integer): The number of pills.
            price (integer): The price of the medicine.
        """        
        self.__name = name
        self.__dosis = dosis
        self.__amount = amount
        self.__price = price
        self.__filled = False
        self.__added_to_bill = False


    def mark_as_filled(self):
        """Mark a medicine object as filled.
        """        
        self.__filled = True

    def mark_as_billed(self):
        """Mark a medicine object as billed.
        """        
        self.__added_to_bill = True

    def __repr__(self):
        """defines how the medical object will be printed.

        Returns:
            string: a string representation of the medicine object.
        """        
        return f'Name: {self.__name}, Filled: {self.__filled}'

    def __eq__(self, other):
        """defines how equality will be checked between medicine objects

        Args:
            other (Medicine): Medicine object 

        Returns:
            Boolean: A True if the objects are 'equal' false if not
        """        
        if self.__name == other.__name and self.__price == other.__price \
                and self.__dosis == other.__dosis and self.__amount == other.__amount:
            return True
        return False

    def get_added_to_bill(self):
        """ get the attribute 'added to bill'

        Returns:
            Boolean: a boolean if the medicine is added to bill.
        """        
        return self.__added_to_bill

    def get_price(self):
        """retrieve the price of the medicine object.

        Returns:
            int: The price of the medicine object.
        """        
        return self.__price


