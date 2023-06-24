class Yotube:
    domain = 'Tech'  # Class Attribute

    def __init__(self, username, subscribers=0):
        self.username = username
        self.subscribers = subscribers


user1 = Yotube('Akash')
print(user1.username)
print(user1.subscribers)
print(user1.domain)
user1.domain = 'Non-Tech'
print(user1.__dict__)

user2 = Yotube('Tejas', 5)
print(user2.username)
print(user2.subscribers)
print(user2.domain)
print(user2.__dict__)


print(Yotube.__dict__)
