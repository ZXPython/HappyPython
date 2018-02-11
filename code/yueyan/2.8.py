class User(object):
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
        print("old login_attempts:{}".format(self.login_attempts))
        print("new login_attempts:{}".format(self.login_attempts + 1))

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("置零:{}".format(self.login_attempts))

class Admin(User):
    def __init__(self,first_name,last_name,number,age,login_attempts):
        super().__init__(first_name,last_name,number,age,login_attempts)
        self.privileges = ["can add post","can delete post","can change post"]
    def show_privileges(self,n):
        print(self.privileges[n])

Admin1 = Admin("wangyueyan", "WANGYUEYAN", "18537511605", "20", 15)
Admin1.describe_user()
Admin1.increment_login_attempts()
Admin1.reset_login_attempts()
Admin1.greet_user()
Admin1.show_privileges(1)
