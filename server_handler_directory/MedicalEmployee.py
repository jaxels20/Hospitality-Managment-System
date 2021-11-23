
class MedicalEmployee:
    """A class to represent a medical employee.
    """
    def __init__(self, username, password, name, role):
        """Constructs all the necessary attributes for the medical employee object.

        Args:
            username (string): The username of the employee.
            password (string): The password of the employee.
            name (string): [The name of the employee.
            role (string): The role of the employee. In current program either 'nurse' or 'doctor'
        """        
        self.__username = username
        self.__password = password
        self.__type = role
        self.__name = name

    def __repr__(self):
        """defines how the medical employee objects will be presented

        Returns:
            [type]: [description]
        """        
        return f"Name: {self.__name}, Username: {self.__username}"

    def __eq__(self, other):
        """The bulit in function which defines how the equality will be checked between medical employee objects.

        Args:
            other ([MedicalEmployee): The medical employee object you would like to compare self to.

        Returns:
            Boolean: True if the username is equal and false if not.
        """        
        if self.__username == other.__username:
            return True
        return False

    def get_username(self):
        """retrieve the username of a specfic medical employee.

        Returns:
            string: a string which is the username of the medical employee.
        """        
        return self.__username

    def get_password(self):
        """retrieve the password of a specfic medical employee.

        Returns:
            string: a string which is the password of the medical employee.
        """    
        return self.__password