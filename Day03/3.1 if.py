#1. 简单例子
cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())

#2. 条件测试
#2.1检查是否相等
car='bmw'
car=='bmw'
car=='audi'

#2.2检查是否相等时不考虑大小写
car='Audi'
car=='audi'
car.lower()=='audi'
car

#2.3检查是否不相等
requested_topping='mushrooms'
if requested_topping!='anchovies':
    print("Hold the anchovies")

#2.4比较数字
age=18
age==18

answer=17
if answer!=42:
    print("that is not the correct answer. Please try again!")

age=19
age<21
age<=21
age>21
age>=21

#2.5检查多个条件
#使用and检查多个条件
age_0=21
age_1=18
(age_0>=20) and (age_1>=20)

#使用or检查多个条件
age_0=21
age_1=18
age_0>=20 or age_1>=20


#2.6检查特定值是否包含在列表中
requested_topping=['mushrooms','onions','pineapple']
'mushrooms' in requested_topping
'pepperroni' in requested_topping

#2.7检查特定值是否不包含在列表中
banned_users=['andrew','carolina','david']
user='marie'
if user not in banned_users:
    print(user.title()+", you can post a response if you wish.")

#2.8布尔表达式--条件测试的别名

#3. if语句
#3.2简单的if语句
age=19
if age>=18:
    print("you are old enough to vote!")

#3.2if-else语句
age=17
if age>=18:
    print("you are old enough to vote!")
else:
    print("sorry, you are too young to vote.")

#3.3if-elif-else结构
age=12
if age<4:
    print("your admission cost is 0.")
elif age<18:
    print("your admission cost is 5.")
else:
    print("your admission cost is 10.")

age=12
if age<4:
    price=0
elif age<18:
    price=5
else:
    price=10
print("your admission cost is"+str(price)+".")

#3.4使用多个elif代码块
age=12
if age<4:
    price=0
elif age<18:
    price=5
elif age<65:
    price=10
else:
    price=5
print("your admission cost is"+str(price)+".")

#3.5省略else代码块
age=12
if age<4:
    price=0
elif age<18:
    price=5
elif age<65:
    price=10
elif age>=65:
    price=5
print("your admission cost is"+str(price)+".")
#else是一条包罗万象的语句，可以考虑用elif来代替以防其他无效数据

#3.6测试多个条件
requested_topping=['mushrooms','extra cheese']
if 'mushrooms' in requested_topping:
    print("adding mushrooms")
if'pepperoni' in requested_topping:
    print("adding pepperoni")
if"extra cheese" in requested_topping:
    print("adding extra cheese")
print("\nFinished making your pizza")

#3.7练习
alien_color='green'
if alien_color=="green":
    print("you get 5 points")

alien_color='yellow'
if alien_color=='green':
    print("you get 5 points for killing a"+alien_color+"alien.")
else:
    print("you get 10 points")

alien_color='green'
if alien_color=='yellow':
    print("you get 10 points for killing a"+alien_color+"alien.")
elif alien_color=='red':
    print("you get 15 points for killing a"+alien_color+"alien.")
else:
    print("you get 5 points for killing a" + alien_color + "alien.")

age=19
if age<2:
    stage='infant'
elif age<4:
    stage='toddler'
elif age<13:
    stage='children'
elif age<20:
    stage='teenager'
elif age<65:
    stage='adult'
else:
    stage='older'
print("you are"+stage)

favorite_fruits=['banana','apple','peach']
if 'banana' in favorite_fruits:
    print("you really like bananas!")
if 'strawberry' in favorite_fruits:
    print("you really like strawberry!")
if 'peach' in favorite_fruits:
    print("you really like peach!")

#4. 使用if语句处理列表
#4.1检查特殊元素
requested_toppings=['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    print("adding "+requested_topping+".")
print("\nFinished making your pizza!")

requested_toppings=['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping=='green peppers':
        print("sorry, we are out of green peppers right now.")
    else:
        print("adding "+requested_topping+".")
print("\nFinished making your pizza!")

#4.2确定列表不是空的
requested_toppings=[]
if requested_toppings:
    for requested_topping in requested_toppings:
        print("adding "+requested_topping+".")
    print("\nFinshied making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#4.3使用多个列表
available_toppings=['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings=['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("adding "+requested_topping+".")
    else:
        print("sorry, we don't have "+requested_topping+".")
print("\nFinished making your pizza!")

#5. 设置if语句的格式
#建议是，在诸如==、>=和<=等比较运算符两边各添加一个空格，方便阅读
