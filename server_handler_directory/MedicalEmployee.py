
class MedicalEmployee:
    def __init__(self, username, password, name, role):
        self.__username = username
        self.__password = password
        self.__type = role
        self.__name = name

    def __repr__(self):
        return self.__name

    def __eq__(self, other):
        if self.__username == other.__username and self.__password == other.__password:
            return True
        return False

