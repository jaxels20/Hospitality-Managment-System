

class Admin:
    """The class wich will be used to represent the admin
    """
    def __init__(self):
        """Constructs all the necessary attributes for the admin object, the username and password is by default set.
        """        
        self.__username = 'admin1'
        self.__password = 'admin1'

    def get_username(self):
        """ Retrieve the username of the admin.

        Returns:
            string: the password of the admin as a string 
        """
        return self.__username

    def get_password(self):
        """retrieve the password of the admin.

        Returns:
            string: the password of the admin
        """        
        return self.__password