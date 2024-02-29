from Post import Factory
from Observer import FollowersObserver


class User:
    def __init__(self, name, password, status):
        self.name = name
        self.password = password
        self.__followingList = []
        self.followersList = []
        self.status = status
        self.posts = []
        self._observer = FollowersObserver(self)
        self.notifications = []

    def follow(self, user):
        if self.status:
            if user not in self.__followingList:
                self.__followingList.append(user)
                user.followersList.append(self._observer)
                print(f"{self.name} started following {user.name}")

    def unfollow(self, user):
        if self.status:
            if user in self.__followingList:
                self.__followingList.remove(user)
                user.followersList.remove(self._observer)
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

    def add_notification(self, string):
        self.notifications.append(string)


    def print_notifications(self):
        print(f"{self.name}'s notifications:")
        for notification in self.notifications:
            print(f"{notification}")

    def notify_all(self):
        for user in self.followersList:
            user.update(self)
