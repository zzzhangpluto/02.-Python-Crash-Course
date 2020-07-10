#1. 函数input()的工作原理
message=input("Tell me something, and i will repeat it back to you: ")
print(message)
#1.1编写清晰的程序
name=input("Please enter your name: ")
print("hello, "+name+"!")
#如果提示超过两行，可以用以下的方式使其清晰
prompt="If you tell us who you are, we can personalize the message you see."
prompt+="\nWhat is your first name?"
name=input(prompt)
print("\nHello, "+name+"!")

#1.2使用int()来获取数值输入
#input得到的是字符串
age=input("How old are you?")
age>=18
age=int(age)
age>=18

height=input("How tall are you, in inches?")
height=int(height)
if height>=36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

#1.3求模运算符%--返回余数
4%3
5%3
7%3
#判断奇偶
number=input("Enter a number, and I'll tell you if it's even or odd: ")
number=int(number)
if number%2==0:
    print("\nThe number "+str(number)+" is even.")
else:
    print("\nThe number "+str(number)+" is odd.")

#1.4练习
car=input("What car do you want to rent?")
print("Let me see if i can find you a "+car+".")

people=input("How many people do you have?")
people=int(people)
if people>8:
    print("Sorry, we cannot satisfy your order")
else:
    print("Your order is accepted.")

number=input("Enter a number, and I'll tell you if it can be divided by 10 ")
number=int(number)
if number%10==0:
    print("\nThe number "+str(number)+" can be divided by 10.")
else:
    print("\nThe number "+str(number)+" cannot be divided by 10.")

#2. while循环
#2.1使用while循环
current_number=1
while current_number<=5:
    print(current_number)
    current_number+=1
print(current_number)

#2.2让用户选择何时退出
prompt="\nTell me something, and I will repeat it back to you:"
prompt+="\nEnter 'quit' to end the program. "
message=""
while message!='quit':
    message=input(prompt)
    print(message)
#改进
prompt="\nTell me something, and I will repeat it back to you:"
prompt+="\nEnter 'quit' to end the program. "
message=""
while message!='quit':
    message=input(prompt)
    if message!='quit':
        print(message)

#2.3使用标志---用来判断整个程序是否处于活动状态的变量
prompt="\nTell me something, and I will repeat it back to you:"
prompt+="\nEnter 'quit' to end the program. "
active=True
while active:
    message = input(prompt)
    if message=='quit':
        active=False
    else:
        print(message)

#2.4使用break退出循环
prompt="\nPlease enter the name of a city you have visited: "
prompt+="\n(Enter 'quit' when you are finished.)"
while True:
    city=input(prompt)
    if city=='quit':
        break
    else:
        print("I'd love to go to "+city.title()+"!")

#2.5在循环中使用continue
current_number=0
while current_number<10:
    current_number+=1
    if current_number%2==0:
        continue
    print(current_number)

#2.6避免无限循环
x=1
while x<=5:
    print(x)
    x+=1

#2.7练习
prompt="\nHow old are you?"
age=""
while age!="quit":
    age=input(prompt)
    if message != 'quit':
        age=int(age)
        if age<3:
            print("\nYou ticket price is 0.")
        elif age<12:
            print("\nYou ticket price is 10.")
        else:
            print("\nYou ticket price is 15.")

prompt="\nHow old are you?"
active=True
while active:
    age = input(prompt)
    if age=='quit':
        active=False
    else:
        age=int(age)
        if age<3:
            print("\nYou ticket price is 0.")
        elif age<12:
            print("\nYou ticket price is 10.")
        else:
            print("\nYou ticket price is 15.")

prompt="\nHow old are you?"
while True:
    age=input(prompt)
    if age=='quit':
        break
    else:
        age=int(age)
        if age<3:
            print("\nYou ticket price is 0.")
        elif age<12:
            print("\nYou ticket price is 10.")
        else:
            print("\nYou ticket price is 15.")

#3. 使用while循环处理列表和字典
#3.1在列表之间移动元素
sandwich_orders=['alice', 'brian', 'candace']
finished_orders=[]
while sandwich_orders:
    finished_order=sandwich_orders.pop()
    print("Verifying user: " + finished_order.title())
    finished_orders.append(finished_order)
print("\nThe following users have been confirmed: ")
for confirmed_user in finished_orders:
    print(confirmed_user.title())

#3.2删除包含特定值的所有列表元素
pets=['cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#3.3使用用户输入来填充字典
responses={}
polling_active=True
while polling_active:
    name=input("\nWhat is your name? ")
    response=input("Which mountain would you like to climb someday?")
    responses[name]=response
    repeat=input("would you like to let another person respond?(Yes/No)")
    if repeat=='No':
        polling_active=False
print("\n---Poll Results---")
for name, response in responses.items():
    print(name+" would like to climb "+response+".")

#3.4练习
sandwich_orders=['tuna', 'chicken', 'beef']
finished_orders=[]
while sandwich_orders:
    finished_order=sandwich_orders.pop()
    print("\nI made your " + finished_order+" sandwich.")
    finished_orders.append(finished_order)
print("\nFinished sandwiches:")
for finished_order in finished_orders:
    print(finished_order+" sandwich")

sandwich_orders=['pastrami','tuna', 'pastrami','chicken','pastrami', 'beef']
print("We have sold out pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

responses={}
polling_active=True
while polling_active:
    name=input("\nWhat is your name? ")
    response=input("If you could visit one place in the world, where would you go?")
    responses[name]=response
    repeat=input("would you like to let another person respond?(Yes/No)")
    if repeat=='No':
        polling_active=False
print("\n---Poll Results---")
for name, response in responses.items():
    print(name+" would like to go "+response+".")
#responses[name]=response这里的name不用引号是因为name已经是一个字符串了，用了引号反而是新建了一个名为name的键
