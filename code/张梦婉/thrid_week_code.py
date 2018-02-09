#1.编写一个名为favorite_book()的函数，其中包含一个名为title的形参，这个函数打印一条消息，
#如one of my favorite books is learn python。调用这个函数,并将一本图书的名字作为实参传递给该函数
def favorite_book(title):
    print(title+':'+'one of my favorite books is learn python')
favorite_book("python")
print("------------------------------------------------------------")


#2.1编写一个名为describe_city的函数，它接受一座城市的名字以及该城市所属的国家。
#这个函数应打印一个简单的例子，如Beijing is in China。
def describe_city(city,country):
    str=city+' is in '+country
    return (str)
print(describe_city('Beijing','China'))
print(describe_city('Vegas','America'))
print("------------------------------------------------------------")
#2.2 给用于存储国家的形参指定默认值，对三个不同的城市调用这个函数，且其中至少有一座城市不属于默认国家
def describe_city(city,country='China'):
    str=city+' is in '+country
    return (str)
print(describe_city('Beijing'))#默认参数
print(describe_city('Vegas','America'))
print(describe_city('Paris','France'))
print("------------------------------------------------------------")

#3.创建一个包含魔术师名字的列表，并将其传递给一个名为show_magicians()的函数，
# 这个函数打印列表中每个魔术师的名字。
list=['qqq','www','aaa','zzz']
def show_magicians(L):
   for i in L:
       print(i)
show_magicians(list)
print("------------------------------------------------------------")

#4.创建一个包含整数的列表，并将其传递给一个名为get_max()和get_min()的函数，输出函数返回的结果
def get_max(List):
    return max(List)
def get_min(List):
    return min(List)
List = [1,5,8,3,4,9,6]
print('最大值是:{}'.format(get_max(List)))
print('最小值是:{}'.format(get_min(List)))
print("------------------------------------------------------------")

# 5创建一个名为User的类，其中包含属性first_name和last_name,自定义其他属性，如年龄，电话等。
# 定义一个名为describe_user()的方法，打印用户信息摘要。定义一个名为greet_user()的方法，
# 它向用户发出个性化的问候，比如hello xxx.创建多个不同用户的实例，对每个实例分别调用上述两个方法
class User(object):
      def __init__(self,first_name,last_name,number,age):
          self.first_name=first_name
          self.last_name=last_name
          self.number=number
          self.age=age
      def describe_user(self):
         print(self.first_name,self.last_name,self.number,self.age,'\t',end='')

      def greet_user(self):

        print('Hello')

user1 = User("zhangmengwan","ZHANGMENGWAN","15036879216","20")
user2 = User("lisa","Lisa","18613753216","21")
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
print("------------------------------------------------------------")

#6.在上一题的基础上，添加一个名为login_attempts的属性，编写一个名为increment_login_attempts()的方法，它将属性login_attempts值加1，
# 编写一个reset_login_attempts()的方法,它将属性login_attempts值重置为0创建一个实例，调用上述方法，检查结果的正确性
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
        print("new login_attempts:{}".format(self.login_attempts + 1))

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("置零:{}".format(self.login_attempts))


user1 = User("zhangmengwan", "ZHANGMENGWAN", "15036879216", "20", 15)
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.reset_login_attempts()
user2 = User("lisa", "Lisa", "18613753216", "21", 20)
user2.describe_user()
user2.greet_user()
user2.increment_login_attempts()
user2.reset_login_attempts()
print("------------------------------------------------------------")

#7.管理员
#管理员是特殊的用户，编写一个名为Admin的类，继承上一题的User类，添加一个privileges的属性，用于存储一个由字符串(如 can add post)组成的列表，编写一个show_privileges()的方法，显示管理员权限
#创建实例并调用该方法
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

Admin1 = Admin("zhangmengwan", "ZHANGMENGWAN", "15036879216", "20", 15)
Admin1.describe_user()
Admin1.increment_login_attempts()
Admin1.reset_login_attempts()
Admin1.greet_user()
Admin1.show_privileges(1)
print("------------------------------------------------------------")
