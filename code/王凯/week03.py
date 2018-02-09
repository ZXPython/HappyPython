# 1. 喜欢的图书
# 编写一个名为favorite_book()的函数，其中包含一个名为title的形参，这个函数打印一条消息，如one of my favorite books is learn python。调用这个函数,并将一本图书的名字作为实参传递给该函数
def favorite_book(title):
    print ('one of my favorite books is '+title+'.')
favorite_book('To be No1')
print('\n')
# 2. 城市
# 2.1 编写一个名为describe_city的函数，它接受一座城市的名字以及该城市所属的国家。这个函数应打印一个简单的例子，如Beijing is in China。
def describe_city(name,nation):
    print(name,'is in',nation)
describe_city('Beijing','China')
# 2.2 给用于存储国家的形参指定默认值，对三个不同的城市调用这个函数，且其中至少有一座城市不属于默认国家
def describe_city(name = 'Beijing1',nation = 'China1'):
    print(name,'is in',nation)
describe_city()
describe_city('Beijing2','China2')
describe_city('Beijing3','China3')
print('\n')
# 3. 魔术师
# 创建一个包含魔术师名字的列表，并将其传递给一个名为show_magicians()的函数，这个函数打印列表中每个魔术师的名字。
def show_magicians(list):
    for i in list:
        print(i)
magicians = ['赵', '钱', '孙', '李']
show_magicians(magicians)
print('\n')
# 4. 最大值和最小值
# 创建一个包含整数的列表，并将其传递给一个名为get_max()和get_min()的函数，输出函数返回的结果
def get_max(list):
        return max(list)
def get_min(list):
        return min(list)
list_x = [12,3,4,5,8,7]
print(get_max(list_x))
print(get_min(list_x))
print('\n')
# 5. 用户
# 创建一个名为User的类，其中包含属性first_name和last_name,自定义其他属性，如年龄，电话等。
# 定义一个名为describe_user()的方法，打印用户信息摘要。定义一个名为greet_user()的方法，
# 它向用户发出个性化的问候，比如hello xxx
# 创建多个不同用户的实例，对每个实例分别调用上述两个方法
class User(object):
    def __init__(self,first_name,last_name,year,tel):
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.tel = tel
    def describe_user(self):
        print('姓名:%s %s\n年龄:%s\n电话:%s' % (self.first_name,
        self.last_name,self.year,self.tel))
    def greet_user(self):
        print('hello '+self.first_name+self.last_name+' !')
User1 = User('No1王','凯',20,110)
User2 = User('李','明',30,120)
User3 = User('王','刚',25,119)
User1.describe_user()
User2.greet_user()
User3.describe_user()
User3.greet_user()
print('\n')
# 6. 尝试登录次数
# 在上一题的基础上，添加一个名为login_attempts的属性，
# 编写一个名为increment_login_attempts()的方法，它将属性login_attempts值加1，
# 编写一个reset_login_attempts()的方法,它将属性login_attempts值重置为0
# 创建一个实例，调用上述方法，检查结果的正确性
class Users(User):
    def __init__(self,first_name,last_name,year,tel,login_attempts):
        super().__init__(first_name,last_name,year,tel)
        self.login_attempts = login_attempts
    def describe_user(self):
        print('姓名:%s %s\n年龄:%s\n电话:%s\n登录次数:%d' % (self.first_name,
        self.last_name,self.year,self.tel,self.login_attempts))
    def greet_user(self):
        print('hello '+self.first_name+self.last_name+' !')
    def increment_login_attempts(self):
        self.login_attempts+= 1
    def reset_login_attempts(self):
        self.login_attempts = 0
Users1 = Users('No2王','凯',20,110,1)
Users1.describe_user()
Users1.increment_login_attempts()
Users1.describe_user()
Users1.reset_login_attempts()
Users1.describe_user()
print('\n')
# 7. 管理员
# 管理员是特殊的用户，编写一个名为Admin的类，继承上一题的User类，
# 添加一个privileges的属性，用于存储一个由字符串(如 can add post)组成的列表，
# 编写一个show_privileges()的方法，显示管理员权限
# 创建实例并调用该方法
class Admin(Users):
    def __init__(self, first_name, last_name, year, tel, login_attempts):
        super().__init__(first_name, last_name, year, tel, login_attempts)
        self.privileges = ["can add post", "can delete post", "can ban user"]
    def show_privileges(self,n):
        print(self.privileges[n])
Admin = Admin('No3王','凯',20,110,0)
Admin.describe_user()
Admin.show_privileges(2)


