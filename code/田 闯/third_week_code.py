# -*- coding:utf-8 -*-
'''
#1.喜欢的图书
#编写一个名为favorite_book()的函数，其中包含一个名为title的形参，这个函数打印一条消息，如one of my favorite books is learn python。调用这个函数,并将一本图书的名字作为实参传递给该函数
'''
def favorite_book(title):
    print("one of my favorite books is learn",title)

book = "Python"
favorite_book(book)



# -*- coding:utf-8 -*-
'''
#2.城市
#2.1 编写一个名为describe_city的函数，它接受一座城市的名字以及该城市所属的国家。这个函数应打印一个简单的例子，如Beijing is in China。
'''
def describe_city(city,country):
    print(city,"is in",country)

describe_city('Beijing','China')

'''
#2.2 给用于存储国家的形参指定默认值，对三个不同的城市调用这个函数，且其中至少有一座城市不属于默认国家
'''
def describe_city1(city,country = "Japan"):
    print(city,country)

describe_city1("Beijing")
describe_city1("Dongjing")
describe_city1("Paris","Franch")



# -*- coding:utf-8 -*-
'''
#3.魔术师
#创建一个包含魔术师名字的列表，并将其传递给一个名为show_magicians()的函数，这个函数打印列表中每个魔术师的名字。
'''
def show_magicians(List):
    for i in List :
        print(i)

List = ["刘谦","石一坚","战神无敌","……"]
show_magicians(List)




# -*- coding:utf-8 -*-
'''
#4.最大值和最小值
#创建一个包含整数的列表，并将其传递给一个名为get_max()和get_min()的函数，输出函数返回的结果
'''
def get_max(List):
    print(max(List))
def get_min(List):
    print(min(List))

List = [1,2.3,6,5,12,-9.32,8]
get_max(List)
get_min(List)




# -*- coding:utf-8 -*-
'''
#5.用户
#创建一个名为User的类，其中包含属性first_name和last_name,自定义其他属性，如年龄，电话等。定义一个名为describe_user()的方法，打印用户信息摘要。定义一个名为greet_user()的方法，它向用户发出个性化的问候，比如hello xxx
#创建多个不同用户的实例，对每个实例分别调用上述两个方法
'''
class User():
    def __init__(self,first_name,last_name,age,telephone):
        self.first_name = first_name
        self.last_name  = last_name
        self.age        = age
        self.tel        = telephone
    def describe_user(self):
        print("info:")
        print("first_name:"+self.first_name)
        print("last_name :"+self.last_name)
        print("age       :"+self.age)
        print("telephone :"+self.tel)
    def greet_user(self):
        print('Hello , Python !')

user1 = User("Tian","Chung","22" ,"15138122561")
user1.describe_user()
user1.greet_user()
user2 = User("Jing","Cha",  "~~~","110"        )
user2.describe_user()
user2.greet_user()



# -*- coding:utf-8 -*-
'''
#6.尝试登录次数
#在上一题的基础上，添加一个名为login_attempts的属性，编写一个名为increment_login_attempts()的方法，它将属性login_attempts值加1，编写一个reset_login_attempts()的方法,它将属性login_attempts值重置为0
#创建一个实例，调用上述方法，检查结果的正确性
'''
class User():
    def __init__(self,first_name,last_name,age,telephone,login_attempts):
        self.first_name     = first_name
        self.last_name      = last_name
        self.age            = age
        self.tel            = telephone
        self.login_attempts = login_attempts
    def describe_user(self):
        print("info:")
        print("first_name:"+self.first_name)
        print("last_name :"+self.last_name)
        print("age       :"+self.age)
        print("telephone :"+self.tel)
    def greet_user(self):
        print('Hello , Python !')
    def increment_login_attempts(self):
        print(self.login_attempts+1)
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)

user1 = User("Tian","Chuang","22" ,"1513812261",13)
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.reset_login_attempts()
user2 = User("Jing","Cha"   ,"~~~","110"       ,27)
user2.describe_user()
user2.greet_user()
user2.increment_login_attempts()
user2.reset_login_attempts()



# -*- coding:utf-8 -*-
'''
#7.管理员
#管理员是特殊的用户，编写一个名为Admin的类，继承上一题的User类，添加一个privileges的属性，用于存储一个由字符串(如 can add post)组成的列表，编写一个show_privileges()的方法，显示管理员权限
#创建实例并调用该方法
'''
class User():
    def __init__(self,first_name,last_name,age,telephone,login_attempts):
        self.first_name     = first_name
        self.last_name      = last_name
        self.age            = age
        self.tel            = telephone
        self.login_attempts = login_attempts
    def describe_user(self):
        print("info:")
        print("first_name:"+self.first_name)
        print("last_name :"+self.last_name)
        print("age       :"+self.age)
        print("telephone :"+self.tel)
    def greet_user(self):
        print('Hello , Python !')
    def increment_login_attempts(self):
        print(self.login_attempts+1)
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)

class Admin(User):
    def __init__(self,first_name,last_name,age,telephone,login_attempts):
        super().__init__(first_name,last_name,age,telephone,login_attempts)
        self.privileges = ["can add post","can delete post","can reset post"]
    def show_privileges(self,n):
        print(self.privileges[n])
admin = Admin("Tian","Chuang","22","15138122561",11)
admin.describe_user()
admin.show_privileges(0)
