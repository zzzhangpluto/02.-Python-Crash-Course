#1. 定义函数
def greet_user():
    """显示简单的问候语"""
    print("Hello")
greet_user()

#1.1向函数传递信息
def greet_user(username):
    """显示简单的问候语"""
    print("Hello, "+username.title()+"!")
greet_user('jessie')

#1.2实参和形参
#username是形参，’jessie‘是实参

#1.3练习
def display_message():
    print("I am learning function")
display_message()

def favorite_book(title):
    print("One of my favorite book is "+title+".")
favorite_book('Alice in Wonderland')

#2. 传递实参
#2.1位置实参--基于实参的顺序，要求实参和形参顺序相同
def describe_pet(animal_type,pet_name):
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet('hamster','harry')
#1)可以调用函数多次
#)位置实参的顺序很重要

#2.2关键字实参---传递给函数的名称-值对
def describe_pet(animal_type,pet_name):
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet(animal_type='hamster',pet_name='harry')
#此时实参的顺序就不重要了

#2.3默认值
def describe_pet(pet_name,animal_type='dog'):
    print("\nI have a "+animal_type+".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='harry')
describe_pet('harry')
#下面的会忽略默认值
describe_pet(animal_type='hamster',pet_name='harry')

#2.4等效的函数调用
describe_pet('harry')
describe_pet(pet_name='harry')
describe_pet('harry','hamster')
describe_pet(animal_type='hamster',pet_name='harry')

#2.5避免实参错误
def describe_pet(animal_type,pet_name):
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet()

#2.6练习
def make_shirt(size,charater):
    print("You ordered a size "+size+" T-shirt with "+charater+".")
make_shirt('s','abc')
make_shirt(size='s',charater='abc')

def make_shirt(size='large',charater='I love python'):
    print("You ordered a size "+size+" T-shirt with "+charater+".")
make_shirt()
make_shirt(size='medium',charater='I love you')

def describe_city(city='Reykjavik',country='Iceland'):
    print(city+" is in "+country+".")
describe_city('hz','China')
describe_city('abc')

#3. 返回值
#3.1返回简单值
def get_formatted_name(first_name,last_name):
    full_name=first_name+' '+last_name
    return full_name.title()
musician=get_formatted_name('jimi','hendrix')
print(musician)

#3.2让实参变成可选的
def get_formatted_name(first_name,middle_name,last_name):
    full_name=first_name+' '+middle_name+' '+last_name
    return full_name.title()
musician=get_formatted_name('john','lee','hooker')
print(musician)
#改为可选：
def get_formatted_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name=first_name + ' ' + last_name
    return  full_name.title()
musician=get_formatted_name('jimi','hendrix')
print(musician)
musician=get_formatted_name('john','lee','hooker')
print(musician)
#python将空字符串解读为true；可选的参数如middle_name必须是最后一个实参

#3.3返回字典
def build_person(first_name,last_name):
    person={'first':first_name,'last':last_name}
    return person
musician=build_person('jimi','hendrix')
print(musician)

def build_person(first_name,last_name,age=''):
    person={'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person
musician=build_person('jimi','hendrix',age=20)
print(musician)

#3.4结合使用函数和while循环
#注意这个循环是无限循环
def get_formatted_name(first_name,last_name):
    full_name=first_name+' '+last_name
    return  full_name.title()
while True:
    print("\nPlease tell me your name: ")
    f_name=input("First Name: ")
    l_name=input("Last name: ")
    formatted_name=get_formatted_name(f_name,l_name)
    print("\nHello, "+formatted_name+"!")
#修改后
def get_formatted_name(first_name,last_name):
    full_name=first_name+' '+last_name
    return  full_name.title()
while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")
    f_name = input("First Name: ")
    if f_name=='q':
        break
    l_name=input("Last Name: ")
    if l_name_=='q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

#3.5练习
def city_country(city,country):
    relation=city+', '+country
    print(relation.title())
city_country('santiago','chile')
city_country('hz','china')
city_country('sh','china')

def make_album(musician,album_name):
    album={'musician':musician,'name':album_name}
    return album
album_1=make_album('abc','bcf')
print(album_1)

def make_album(people,album_name,number=''):
    album={'musician':people,'name':album_name}
    if number:
        album['number']=number
    return album
album_2=make_album('abc','bcf',number=4)
print(album_2)

while True:
    print("\nPlease tell me the musician and album name: ")
    print("(enter 'q' at anytime to quit)")
    musician=input("Musician: ")
    if musician=='q':
        break
    album_name=input("Album name: ")
    if album_name=='q':
        break
    album_0=make_album(musician,album_name)
    print(album_0)

#4. 传递列表
def greet_users(names):
    for name in names:
        msg="Hello, "+name.title()+"!"
        print(msg)
usernames=['hannah','ty','margot']
greet_users(usernames)

#4.1在函数中修改列表
unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]
while unprinted_designs:
    current_desigh=unprinted_designs.pop()
    print("Printing model: "+current_desigh)
    completed_models.append(current_desigh)
print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)
#用函数修改上面的代码：
def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_desigh = unprinted_designs.pop()
        print("Printing model: " + current_desigh)
        completed_models.append(current_desigh)
def show_completed_models(completed_models):
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

#4.2禁止函数修改列表
#将列表的副本传递给函数function_name(list_name[:])
print_models(unprinted_designs[:],completed_models)
#这样会保存unprinted_designs，使用其副本跑函数，但是效率很低

#4.3练习
magicians=['david','pluto','baby','amy']
def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())
show_magicians(magicians)

def make_great(name_list1,name_list2):
    while name_list1:
        name=name_list1.pop()
        name+=" the Great"
        name_list2.append(name)
namelist=[]
make_great(magicians,namelist)
show_magicians(namelist)

def make_great(name_list1,name_list2):
    while name_list1:
        name=name_list1.pop()
        name+=" the Great"
        name_list2.append(name)
namelist=[]
magicians=['david','pluto','baby','amy']
make_great(magicians[:],namelist)
show_magicians(namelist)
show_magicians(magicians)

#5. 传递任意数量的实参
def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("-"+topping)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

#5.1结合使用位置实参和任意数量实参
#如果上一个函数还需要一个size实参，就必须放在*toppings前面，如下：
def make_pizza(size,*toppings):
    print("\nMaking a "+str(size)+"-inch pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping)
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

#5.2使用任意数量的关键字实参
#例子中，我们不知道会收到什么样的info
def build_profile(first,last,**user_info):
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile
user_profile=build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)

#5.3练习
def make_sandwich(*toppings):
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print("-"+topping)
make_sandwich('pepperoni')
make_sandwich('mushrooms','green peppers','extra cheese')

def make_car(brand,size,**car_info):
    profile={}
    profile['brand']=brand
    profile['size']=size
    for key,value in car_info.items():
        profile[key]=value
    return profile
my_car=make_car('subaru','outback',color='blue',tow_package=True)
print(my_car)

#6. 将函数存储在模块中
#6.1导入整个模块
#模块是扩展名为.py的文件，包含要导入到程序中的代码

#6.2导入特定的函数
#from module_name import function_name

#6.3使用as给函数指定别名
from pizza import make_pizza as mp
mp(16.'pepperoni')

#6.4使用as给模块指定别名
import pizza as p
p.make_pizza(16,'pepperoni')
#模块指定别名的通用语法：
#import module_name as mn

#6.5导入模块中的所有函数
from pizza import *

#7. 函数编写指南
#应给函数指定描述性名称，且只在其中使用小写字母和下划线
#每个函数都应包含简要阐述功能的注释，紧跟在函数定义后面，采用文档字符串格式
#给形参指定默认值时，等号两边不要有空格
#代码行长度最好不要超过79字符
#如果程序/模块包含多个函数，可以使用两个空行将相邻的函数分开
#所有的import都应放在文件开头
