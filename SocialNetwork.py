from User import User


class SocialNetwork:
    _instance = None

    def __new__(cls, name_of_app):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name_of_app):
        self.__name_of_app = name_of_app
        self.__my_dict = dict()
        print("The social network " + name_of_app + " was created!")

    def sign_up(self, name, password):
        if len(password) < 4 or len(password) > 8:
            return False
        if name in self.__my_dict:
            return False
        user = User(name, password, True)
        self.__my_dict[name] = user
        return user

    def log_out(self, name):
        if name in self.__my_dict:
            self.__my_dict[name].status = False
            print(f"{name} disconnected")
            return True
        return False

    def log_in(self, name, password):
        if name in self.__my_dict:
            self.__my_dict[name].status = True
            print(f'{name} connected')
            return True
        return False

    def __str__(self):
        result = f"{self.__name_of_app} social network:\n"
        for name, user in self.__my_dict.items():
            result += (f"User name: {name}, Number of posts: {len(user.posts)},"
                       f" Number of followers: {len(user.followersList)}\n")
        return result.rstrip() + '\n'
