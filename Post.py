from matplotlib import image as mpimg
import matplotlib.pyplot as plt


class Post:
    def __init__(self, post_type, content, user):
        self.post_type = post_type
        self.content = content
        self.user = user
        self.likes = 0
        self.comments = []

        self.user.notify_all(user, f"{user.name} has a new post")  # Notifying on a post

    def like(self, user):
        if user.status:
            self.likes += 1
            self.user.notify_user(self.user, user, f'{user.name} liked your post', True)

    def comment(self, user, comment: str):
        if user.status:
            comment_text = f"{user.name}: {comment}"
            self.comments.append(comment_text)
            self.user.notify_user(self.user, user, f'{user.name} commented on your post', True, f"{comment}")


class TextPost(Post):
    def __init__(self, content, user):
        super().__init__("Text", content, user)

    def __str__(self):
        return f"{self.user.name} published a post:\n" f"\"{self.content}\"\n"


class ImagePost(Post):
    def __init__(self, content, user):
        super().__init__("Image", content, user)

    def display(self):
        img = mpimg.imread(self.content)
        plt.imshow(img)
        plt.show()
        print("Shows picture")

    def __str__(self):
        return f"{self.user.name} posted a picture\n"


class SalePost(Post):
    def __init__(self, content, user, price, location):
        super().__init__("Sale", content, user)
        self.price = price
        self.location = location
        self.available = True

    def discount(self, discount, password):
        if self.available and self.user.check_password(password):
            self.price = self.price - (self.price * (discount / 100))
            print(f"Discount on {self.user.name} product! the new price is: {self.price}")

    def sold(self, password):
        if self.user.check_password(password) and self.available:
            self.available = False
            print(f"{self.user.name}'s product is sold")

    def __str__(self):
        return f"{self.user.name} posted a product for sale:\n" \
               f"Sold! {self.content}, price: {self.price}, pickup from: {self.location}\n"


class Factory:
    @staticmethod
    def build_post(types, content, user, price=None, location=None):
        if types == "Text":
            return TextPost(content, user)
        elif types == "Image":
            return ImagePost(content, user)
        elif types == "Sale":
            return SalePost(content, user, price, location)
