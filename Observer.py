from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, other):
        pass


class FollowersObserver(Observer):
    def __init__(self, user):
        self.user = user

    def update(self, user):
        string = f"{user.name} has a new post"
        self.user.add_notification(string)
