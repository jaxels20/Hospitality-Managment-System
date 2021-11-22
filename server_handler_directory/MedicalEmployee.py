
class MedicalEmployee:
    """
    A class to represent a medical employee
    ...

    Attributes
    -----------
    username : str
        the username of the employee
    password : str
        the username of the employee
    type : str
        the role of the employee, either a doctor or a nurse
    name : str

    Methods
    _______
    get_username():
        returns the username of the admin
    get_password():
        returns the password of the admin
    """
    def __init__(self, username, password, name, role):
        self.__username = username
        self.__password = password
        self.__type = role
        self.__name = name

    def __repr__(self):
        return f"Name: {self.__name}, Username: {self.__username}"

    def __eq__(self, other):
        if self.__username == other.__username:
            return True
        return False

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password