

class Admin:
    """
    A class to represent the admin.
    ...

    Attributes
    ----------
    username : str
        the username of the admin
        by default sat to 'admin1'
    password : str
        the password for the admin
        by default sat to 'admin1'

    Methods
    -------
    get_username():
        returns the username of the admin
    get_password():
        returns the password of the admin
    """
    def __init__(self):
        """
        Constructs all necessary attributes
        """
        self.__username = 'admin1'
        self.__password = 'admin1'

    def get_username(self):
        """
        retrieve the username of the admin
        ...
        :return:
        the username of the admin
        """
        return self.__username

    def get_password(self):
        """
        retrieve the password of the admin
        ...
        :return:
        the password of the admin
        """
        return self.__password