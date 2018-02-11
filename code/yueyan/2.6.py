class User():
      def __init__(self,first_name,last_name,number,age):
          self.first_name=first_name
          self.last_name=last_name
          self.number=number
          self.age=age
      def describe_user(self):
         print(self.first_name,self.last_name,self.number,self.age,'\t',end='')

      def greet_user(self):

        print('ni')

user1 = User("wangyueyan","WANGYUEYAN","15836911605","20")
user2 = User("aa","AA","18537511360","20")
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
