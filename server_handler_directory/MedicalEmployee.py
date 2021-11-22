
class MedicalEmployee:
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