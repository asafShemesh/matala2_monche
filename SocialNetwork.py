from User import User


class SocialNetwork:
    _instance = None

    def __new__(cls, name_of_app):
        if cls._instance is None:  # If the instance don't exist
            cls._instance = super().__new__(cls)  # Create a new one with the 'new' of The father's department
        return cls._instance

    def __init__(self, name_of_app):
        self.__name_of_app = name_of_app
        self.__my_dict = dict()
        print("The social network " + name_of_app + " was created!")

    def sign_up(self, name, password):
        if len(password) < 4 or len(password) > 8:  # If the password does not match the conditions
            return False
        if name in self.__my_dict:  # If the name is in the dict (the "name list")
            return False
        user = User(name, password)
        self.__my_dict[name] = user
        #  self.my_dict.update(name)  # We add the name to the dict, now we have a new user registered
        return user

# TODO : check this function
    def log_out(self, name):
        if name in self.__my_dict:  # If the name is connected, and he wants to disconnect
            del self.__my_dict[name]  # We will delete his name from the list$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            return True
        return False

    def log_in(self, name, password):
        if self.sign_up(name, password) in self.__my_dict:  # If the name is in the dict
            return True  # Its means that he is connected
        return False

    # TODO : check if i need this function
    def print_notifications(self):
        return False




