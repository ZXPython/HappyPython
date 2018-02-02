#No1
print('hello world')
#No2
h = 'hello world'
print(h)
#No3
name = "wang kai"
print(name.upper())
print(name.lower())
print(name.title())
#No4
name = '  John Smith  '
print (name.replace(' ',''))
#No5
print(10+10)
print(10*2)
print(30-10)
print(20//1)
#No6
n = 1
while n<=20:
    print(n,end=" ")
    n = n+1
print("")
#No7
t = []
n = 1
while n<=1000:
        if (n % 4) == 0:
            t.append(n)
        n = n+1
print(t)
#No8
s=[]
n = 1
while n<=20:
    s.append(n*n*n)
    n = n+1
for n in range(20):
  print(s[n],end=" ")
print("")
#No9
x = 1
y = 1
for x in range(1,10):
    for y in range(1,x+1):
        print("%d*%d=%d"%(x,y,x*y),end=" ")
    print("")
#No10
num = int(input("输入一个数字: "))
if (num % 2) == 0:
   print("{0} 是偶数".format(num))
else:
   print("{0} 是奇数".format(num))
#No11
age = int(input("请输入年龄:"))
if age<2:
    print("婴儿")
else:
    if age<4:
        print("蹒跚走路")
    else:
        if age<13:
            print("儿童")
        else:
            if age<20:
                print("青少年")
            else:
                if age<65:
                    print("成年人")
                else:
                    print("老年人")
#No12
list=[]
for numbers in range(1,10):
    list.append(numbers)
print(list)
for number in list:
    if number==1:
        print(str(number)+'st')
    elif number==2:
        print(str(number)+'nd')
    elif number==3:
        print(str(number)+'rd')
    else:
        print(str(number)+'th')
#No13
citys = {
    'city1' : {
    'country':'country1',
    'num':'1'
    },
    'city2':{
    'country':'country2',
    'num':'2'
    },
    'city3':{
    'country':'country3',
    'num':'3'
    },
}
for key,value in citys.items():
    print(key+":")
    for key1,value2 in value.items():
        print("\t %s:%s"%(key1,value))
