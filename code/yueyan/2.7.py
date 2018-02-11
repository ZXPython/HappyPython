class User():
    def __init__(self, first_name, last_name, number, age, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.age = age
        self.login_attempts = login_attempts

    def describe_user(self):
        print("first_name:{}".format(self.first_name))
        print("last_name:{}".format(self.last_name))
        print("telephone number:{}".format(self.number))
        print("age:{}".format(self.age))

    def greet_user(self):
        print('Hello {}'.format(self.first_name))

    def increment_login_attempts(self):
        print("new login_attempts:{}".format(self.login_attempts + 1))

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("置零:{}".format(self.login_attempts))


user1 = User("wangyueyan", "WANGYUEYAN", "15036879216", "20", 11)
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.reset_login_attempts()
user2 = User("aa", "AA", "8537511360", "20", 19)
user2.describe_user()
user2.greet_user()
user2.increment_login_attempts()
user2.reset_login_attempts()
