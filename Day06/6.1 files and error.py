#1. 从文件中读取数据
#1.1读取整个文件
with open('pi_digits.txt') as file_object:
    contents=file_object.read()
    print(contents)
#read()到达文件末尾时返回一个空字符串，显示出来就是空行，可以用rstrip剥除
with open('pi.digits.txt') as file_object:
    contents=file_object.read()
    print(contents.rstrip())

#1.2逐行读取
filename='pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)

#1.3创建一个包含文件各行内容的列表
filename='pi_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
for line in lines:
    print(line.rstrip())

#1.4使用文件的内容
filename='pi_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
pi_string=''
for line in lines:
    pi_string+=line.rstrip()
print(pi_string)
print(len(pi_string))

#1.5包含一百万位的大型文件
filename='pi_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
pi_string=''
for line in lines:
    pi_string+=line.strip()
print(pi_string[:52]+"...")
print(len(pi_string))

#1.6圆周率值中包含你的生日吗
filename='pi_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
pi_string=''
for line in lines:
    pi_string+=line.strip()
birthday=input("Enter your birthday, in form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi!")

#2. 写入文件
#2.1写入空文件
filename='programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love programming.")
#实参'w'是写入模式，'r'是读取，'a是附加，'r+'是读取和写入，默认是只读


#2.2写入多行
filename='programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.")

#2.3附加到文件
filename='programming.txt'
with open(filename,'a') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.")

#3. 异常
#3.1处理ZeroDivisionError
print(5/0)

#3.2使用try-except代码块
try:
    print(5/0)
except ZeroDivisionError:
    print("You cannot divide by zero!")

#3.3使用异常避免崩溃
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number=input("\nFirst number: ")
    if first_number=='q':
        break
    second_number=input("\nSecond number: ")
    if second_number=='q':
        break
    answer=int(first_number)/int(second_number)
    print(answer)
#如果0是second_number，程序会崩溃

#3.4else代码块
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number=input("\nFirst number: ")
    if first_number=='q':
        break
    second_number=input("\nSecond number: ")
    if second_number=='q':
        break
    try:
        answer=int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You cannot divide by 0!")
    else:
        print(answer)

#3.5处理FileNotFoundError异常
filename='alice.txt'
try:
    with open(filename) as file_object:
        contents=file_object.read()
except FileNotFoundError:
    msg="Sorry, the file "+filename+" does not exist."
    print(msg)

#3.6分析文本
title="Alice in Wonderland"
title.split()
#计算aiw有多少个单词
filename='alice.txt'
try:
    with open(filename) as file_object:
        contents=file_object.read()
except FileNotFoundError:
    msg="Sorry, the file "+filename+" does not exist."
    print(msg)
else:
    #计算文件大致包含多少个单词
    words=contents.split()
    num_words=len(words)
    print("The file "+filename+" has about "+str(num_words)+" words")

#3.7使用多个文件
def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words")
filenames=['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
for filename in filenames:
    count_words(filename)

#3.8失败时什么都不做
def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words")

#4. 存储数据
#4.1使用json.dump()和json.load()
import json
numbers = [2, 3, 5, 7, 11, 13]
filename='numbers.json'
with open(filename,'w') as file_object:
    json.dump(numbers,file_object)

import json
filename='numbers.json'
with open(filename,'w') as file_object:
    numbers=json.load(file_object)
print(numbers)

#4.2保存和读取用户生成的数据
import json
username=input("What is your name?")
filename='username.json'
with open(filename,'w') as file_object:
    json.dump(username,file_object)
    print("We'll remember you when you come back, "+username+"!")

import json
filename='username.json'
with open(filename) as file_object:
    username=json.load(file_object)
    print("Welcome back, "+username+"!")

import json
#如果以前存储了用户名，就加载，否则，就提示用户输入
filename='username.json'
try:
    with open(filename) as file_object:
        username=json.load(file_object)
except FileNotFoundError:
    username=input("What is your name?")
    with open(filename,'w') as file_object:
        json.dump(username, file_object)
        print("We'll remember you when you come back, "+username+"!")
else:
    print("Welcome back, "+username+"!")

#4.3重构--将代码划分为一系列完成具体工作的函数
import json
def greet_user():
    """问候用户，并指出其名字"""
    filename = 'username.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        username = input("What is your name?")
        with open(filename, 'w') as file_object:
            json.dump(username, file_object)
            print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")
greet_user()
#重构
import json
def get_stored_username():
    """如果存储了用户名，就获取"""
    filename = 'username.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    """问候用户，并指出其名字"""
    username=get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = input("What is your name?")
        filename = 'username.json'
        with open(filename, 'w') as file_object:
            json.dump(username, file_object)
            print("We'll remember you when you come back, " + username + "!")
greet_user()
#更进一步的
import json
def get_stored_username():
    """如果存储了用户名，就获取"""
    filename = 'username.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
    return username

def greet_user():
    """问候用户，并指出名字"""
    username=get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")
greet_user()