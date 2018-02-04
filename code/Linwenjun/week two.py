#10
num =int(input("请输入："))
if num %2==0:
    print(str(num)+"是偶数")
else:
    print(str(num)+"是奇数")
#11
age=int(input("请输入年龄："))
if age<0:
    print("输入错误")
elif age in range(2,4):
    print("他是婴儿")
elif age in range(2,4):
    print("他正蹒跚走路")
elif age in range(4,13):
    print("他是儿童")
elif age in range(13,20):
    print("他是青少年")
elif age in range(20,65):
    print("他是成年人")
else:
    print("他是老年人")
#12
L=[]
L=range(1,10)
for i in L:
    if i==1:
        print(str(i)+"-"+str(i)+"st")
    elif i==2:
        print(str(i)+"-"+str(i)+"nd")
    elif i==3:
        print(str(i)+"-"+str(i)+"rd")
    else:
        print(str(i)+"-"+str(i)+"th")
#13
citys={'fuzhou':{'country':'China','number':1000000},
       'henan':{'country':'China','number':8000000},
      'shanghai':{'country':'China','number':3000000}}
for i in citys:
    print(i+':'+str(citys[i]))