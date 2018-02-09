#1
def favorite_book(title):
    print(title,'one of my favorite books is learn python')
favorite_book('红楼梦')
#2.1
def describe_city(city,country):
    print(city ,'is in',country)
describe_city('Beijing','China')
#2.2
def describe_city(city,country='China'):
    print(city,'is in',country)
describe_city('Fuzhou')
describe_city('Shanghai')
describe_city('New York','America')
#3
Magicians=['Tony','Moble','Nike']
def show_magicians(Magicians):
    print(Magicians)
show_magicians(Magicians)
#4
L=[1,2,3]
def git_max(L):
    s=1
    for i in range(1,len(L)+1):
        if i>s:
            s=i
    print(s)
def git_min(L):
    s=1
    for i in range(1,len(L)+1):
        if s<i:
            i=s
    print(i)
git_max(L)
git_min(L)
#5
class User():
    def __init__(self,fist_name,last_name,age,tel):
        self.fist_name=fist_name
        self.last_name=last_name
        self.age=age
        self.tel=tel
    def describe_user(self):
        print('fist name:'+self.fist_name)
        print('last name:'+self.last_name)
        print('      age:'+self.age)
        print('      tel:'+self.tel)
    def greet_user(self):
        print('hello '+self.last_name)
L=User('L','Lisa','18','1234567')
L.describe_user()
L.greet_user()
M=User('M','Mobe','19','2502544')
M.describe_user()
M.greet_user()
#6
class User():
    def __init__(self, fist_name, last_name, age, tel, login_attempts):
        self.fist_name=fist_name
        self.last_name=last_name
        self.age=age
        self.tel=tel
        self.login_attempts=login_attempts
    def describe_user(self):
        print('fist name:'+self.fist_name)
        print('last name:'+self.last_name)
        print('      age:'+self.age)
        print('      tel:'+self.tel)
    def greet_user(self):
        print('hello '+self.last_name)
    def increment_login_attempts(self):
        print(self.login_attempts+1)
    def reset_login_attempts(self):
        self.login_attempts=0
        print(self.login_attempts)
L=User('L','Lisa','18','1234567',1)
L.describe_user()
L.greet_user()
L.increment_login_attempts()
L.reset_login_attempts()
M=User('M','Mobe','19','2502544',2)
M.describe_user()
M.greet_user()
M.increment_login_attempts()
M.reset_login_attempts()
#7
class Admin(User):
    def __init__(self,fist_name,last_name,age,tel,login_attempts):
        super().__init__(fist_name, last_name, age, tel, login_attempts)
        self.privileges=['can add post']
    def show_privileges(self,):
        print(self.privileges[0])
L=Admin("L","Lisa","18","1234567",1)
L.describe_user()
L.greet_user()
L.increment_login_attempts()
L.reset_login_attempts()
L.show_privileges()