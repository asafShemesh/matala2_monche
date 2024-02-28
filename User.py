from Post import Factory


class User:
    def __init__(self, name, password, status):
        self.name = name
        self.password = password
        self.__followingList = []
        self.followersList = []
        self.status = status
        self.posts = []
        self._notifications = []

    def follow(self, user):
        if self.status:
            if user not in self.__followingList:
                self.__followingList.append(user)
                user.followersList.append(self)
                print(f"{self.name} started following {user.name}")

    def unfollow(self, user):
        if self.status:
            if user in self.__followingList:
                self.__followingList.remove(user)
                user.followersList.remove(self)
                print(f"{self.name} unfollowed {user.name}")

    def check_password(self, password):
        return password == self.password

    def publish_post(self, post_type, content, price=None, location=None):
        if self.status:
            if price is not None and location is not None:
                new_post = Factory.build_post(post_type, content, self, price, location)
                print(f"{self.name} posted a product for sale:")
                print(f"For sale! {content}, price: {price}, pickup from: {location}\n")
            else:
                new_post = Factory.build_post(post_type, content, self)
                if post_type != "Image":
                    print(f"{self.name} published a post:")
                    print(f"\"{content}\"\n")
                else:
                    print(f"{self.name} posted a picture\n")

            self.posts.append(new_post)
            return new_post

        else:
            return None

    def __str__(self):
        return f"User name: {self.name}, Number of posts: {len(self.posts)}, Number of followers: {len(self.followersList)}"

    def notify(self, message: str, flag: bool, more_message: str):
        self._notifications.append(message)

        if flag and more_message == "":
            print(f"notification to {self.name}: {message}{more_message}")
        elif flag:
            print(f"notification to {self.name}: {message}: {more_message}")

    def print_notifications(self):
        print(f"{self.name}'s notifications:")
        for notify in self._notifications:
            print(notify)

    def notify_user(self, user_to_notify, notifier, message, flag: bool = False,
                    extra_message: str = "") -> None:
        if user_to_notify == notifier:
            return
        user_to_notify.notify(message, flag, extra_message)

    def notify_all(self, notifier, message, flag: bool = False):
        for user in notifier.followersList:
            self.notify_user(user, notifier, message, flag)
