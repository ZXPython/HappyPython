#1.使用print语句，输出hello world
print('hello world')

#2.将hello world 赋值给一个变量，输出
a = 'hello world'
print(a)


#3.将一个人名存储到变量中，以小写，大写和首字母大写的方式显示这个人名
name = 'john'
print(name.lower())
print(name.upper())
print(name.title())


#4.name = ' John Smith ',使用相关函数将开头，结尾，开头和结尾和空格去掉并打印结果
name = ' John Smith '
s1 = name.lstrip()
s2 = name.rstrip()
s3 = name.strip()
s4 = name.replace(' ', '')
print(s1 + '\n' + s2 + '\n' + s3 + '\n' + s4)




#5.编写4个表达式，分别使用 + - * / ，使其结果为20，比如print(10 + 10)
print(10 + 10)
print(30 - 10)
print(5 * 4)
print(40 // 2)


#6.使用for循环打印数字1~20，包含20
for x in range(1, 21):
    print(x)


#7.创建一个列表，其中包括1-1000能被4整除的数字，使用for循环将这个列表中的数字打印出来
numbers = []
for num in range(1, 1001):
    if num % 4 == 0:
        numbers.append(num)
print(numbers)


#8.创建一个列表，包括1-20这20个数的立方值，使用for循环将这个列表中的数字打印出来
numbers = []
for num in range(1, 21):
    number = num ** 3
    numbers.append(number)
print(numbers)


#9.打印九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print("%d*%d=%2d" % (i, j, i*j), end=" ")
    print(" ")


#10.给出一个变量num，判断其是奇数还是偶数，并输出
num = int(input("please input:"))
if (num % 2) == 0:
    print(str(num) + ' is even number')
else:
    print(str(num) + ' is uneven number')


#11.设置age变量，使用if-elif-else结构，根据age值判断处于人生哪个阶段，小于2岁，输出他是婴儿,2(含)-4岁，输出他正蹒跚走路,4(含)-13岁，
 输出他是儿童，13(含)-20岁，输出他是青少年，20(含)-65岁，输出他是成年人,大于等于65岁，输出他是老年人
age = int(input("please input:"))
if 0 <= age < 2:
    print('He is a baby')
elif 2 <= age < 4:
    print('He is a toddler')
elif 4 <= age < 13:
    print('He is a child')
elif 13 <= age < 20:
    print('He is a teenager')
elif 20 <= age < 65:
    print('He is an adult')
else:
    print('He is an older')


#12.序数表示位置,如1st和2nd，在一个列表中存储数字1-9,遍历这个列表，
 输出这个数字和对应的序数,格式为1-1st,每个数字占一行
num = []
for numbers in range(1, 10):
    num.append(numbers)
for number in num:
    if number == 1:
        print(str(number) + '-' + str(number)+'st')
    elif number == 2:
        print(str(number) + '-' + str(number)+'nd')
    elif number == 3:
        print(str(number) + '-' + str(number)+'rd')
    else:
        print(str(number) + '-' + str(number)+'th')


#13.创建一个名为citys的字典，其中将三个城市名用作键，对于每个城市，分别创建一个字典，
 包括两个键，country和number，表示所属国家和城市人口，将每座城市和他们的信息输出
citys = {'Beijing': [{'country': 'China', 'number': '1961.24万'}],
         'London': [{'country': 'England', 'number': '861.50万'}],
         'Boston': [{'country': 'America', 'number': '62.51万'}]
         }
for key in citys:
    print(key + ':' + str(citys[key]))
