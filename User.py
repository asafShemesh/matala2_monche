class User:

    def __init__(self, name, password,status):
        self.name = name
        self.password = password
        self.__followinglist = []  # List of users self follow
        self.__followerslist = []  # List of users that follow after self

    def update(self):
        pass

    def follow(self, user):
        if user not in self.__followinglist:  # If self isn't follow after user
            self.__followinglist.append(user)  # We will add user to the list of followers of self
            user.__followerslist.append(self)  # We will add self

    def unfollow(self, user):
        if user in self.__followinglist:  # If self follow after user
            user.__followinglist.remove(self)  # Remove self from the list of users that user follow
            self.__followerslist.remove(user)  # Remove user from the list that follow after self








