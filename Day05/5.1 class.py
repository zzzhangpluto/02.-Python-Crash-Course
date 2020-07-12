#1. 创建和使用类
#1.1创建Dog类
class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self, name,age):
        """初始化属性name和age"""
        self.name=name
        self.age=age
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title()+" is now sitting.")
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title()+" rolled over!")

#1.2根据类创建实例
class Dog():
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")
my_dog=Dog('willie',6)
print("My dog's name is "+my_dog.name.title()+".")
print("My do is "+str(my_dog.age)+" years old.")

#访问属性
my_dog.name
#调用方法
my_dog.sit()
my_dog.roll_over()
#创建多个实例
class Dog():
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")
my_dog=Dog('willie',6)
your_dog=Dog('lucy',3)
print("My dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old.")
my_dog.sit()
print("Your dog's name is "+your_dog.name.title()+".")
print("Your dog is "+str(your_dog.age)+" years old.")
your_dog.sit()

#1.3练习
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name=restaurant_name
        self.type=cuisine_type

    def describe_restaurant(self):
        print(self.name.title()+" is a "+self.type+" restaurant.")

    def open_restaurant(self):
        print(self.name.title()+" now is open.")

restaurant_1 = Restaurant('panda', 'Chinese')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

restaurant_2=Restaurant('abc',"Italy")
restaurant_3=Restaurant('bcf','Thailand')
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

class User():
    def __init__(self, first_name, last_name):
        self.fn=first_name
        self.ln=last_name
    def describe_user(self):
        print("User's name is "+self.fn.title()+" "+self.ln.title()+".")
    def greet_user(self):
        print("Hello, "+self.fn.title()+" "+self.ln.title()+".")

user_1=User('lucy','white')
user_2=User('Amy','Lee')
user_3=User('Paul','Wang')
user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()
user_3.describe_user()
user_3.greet_user()

#2. 使用类和实例
#2.1Car类
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make=make
        self.model=model
        self.year=year
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=str(self.year)+' '+self.make+' '+self.model
        return  long_name.title()
my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

# 2.2给属性指定默认值
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=str(self.year)+' '+self.make+' '+self.model
        return  long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 2.3修改属性的值
#有三种方法修改，直接通过实例修改，通过方法进行设置，通过方法进行递增
#1)直接修改属性的值
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=str(self.year)+' '+self.make+' '+self.model
        return  long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading=23
my_new_car.read_odometer()

#2)通过方法修改
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=str(self.year)+' '+self.make+' '+self.model
        return  long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):
        self.odometer_reading=mileage

my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()
#可以再添加逻辑禁止任何人将里程表读书回调
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=str(self.year)+' '+self.make+' '+self.model
        return  long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):
        """将里程表读书设置为指定值，禁止回调"""
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You cannot roll back on odometer!")

#3)通过方法对属性的值递增
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=str(self.year)+' '+self.make+' '+self.model
        return  long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):
        self.odometer_reading=mileage
    def increment_odometer(self,miles):
        """将里程表读书增加指定的量"""
        self.odometer_reading+=miles
my_used_car=Car('subaru','outback',2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# 2.4练习
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        print(self.name.title() + " is a " + self.type + " restaurant.")

    def open_restaurant(self):
        print(self.name.title() + " now is open.")

    def served_number(self):
        return str(self.number_served)

restaurant_1 = Restaurant('panda', 'Chinese')
restaurant_1.served_number()


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.name.title() + " is a " + self.type + " restaurant.")

    def open_restaurant(self):
        print(self.name.title() + " now is open.")

    def served_number(self):
        return str(self.number_served)

    def set_number_served(self,number):
        self.number_served=number
        print(self.number_served)


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.name.title() + " is a " + self.type + " restaurant.")

    def open_restaurant(self):
        print(self.name.title() + " now is open.")

    def served_number(self):
        return str(self.number_served)

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self,added):
        self.number_served+=added

restaurant_1 = Restaurant('panda', 'Chinese')
restaurant_1.set_number_served(3)
restaurant_1.served_number()
restaurant_1.increment_number_served(5)
restaurant_1.served_number()

#尝试登录次数
class User():
    def __init__(self, first_name, last_name):
        self.fn=first_name
        self.ln=last_name
        self.login_attemps=0
    def describe_user(self):
        print("User's name is "+self.fn.title()+" "+self.ln.title()+".")
    def greet_user(self):
        print("Hello, "+self.fn.title()+" "+self.ln.title()+".")
    def read_attemps(self):
        print(str(self.login_attemps))
    def increment_login_attemps(self):
        self.login_attemps+=1
    def reset_login_attemps(self):
        self.login_attemps=0
user_1=User('lucy','white')
user_1.read_attemps()
user_1.increment_login_attemps()
user_1.read_attemps()
user_1.increment_login_attemps()
user_1.read_attemps()
user_1.reset_login_attemps()
user_1.read_attemps()

# 3. 继承
# 3.1子类的方法__init__()
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=str(self.year)+' '+self.make+' '+self.model
        return  long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):
        """将里程表读书设置为指定值，禁止回调"""
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You cannot roll back on odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,model,year)

my_tesla=ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())

# 3.2给子类定义属性和方法
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=str(self.year)+' '+self.make+' '+self.model
        return  long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):
        """将里程表读书设置为指定值，禁止回调"""
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You cannot roll back on odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self,make,model,year):
        """初始化父类的属性，再初始化电动汽车特有属性"""
        super().__init__(make,model,year)
        self.battery_size=70
    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kw battery.")
my_tesla=ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# 3.2重写父类的方法
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self,make,model,year):
        """初始化父类的属性，再初始化电动汽车特有属性"""
        super().__init__(make,model,year)
        self.battery_size=70
    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kw battery.")
    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car does not need a gas tank!")

# 3.4将实例用作属性
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=str(self.year)+' '+self.make+' '+self.model
        return  long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):
        """将里程表读书设置为指定值，禁止回调"""
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You cannot roll back on odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles
class Battery(Car):
    def __init__(self,battery_size=70):
        self.battery_size=battery_size
    def describe_battry(self):
        print("This car has "+str(self.battery_size)+"-kw battery.")
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self,make,model,year):
        """初始化父类的属性，再初始化电动汽车特有属性"""
        super().__init__(make,model,year)
        self.battery=Battery()
my_tesla=ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

class Battery(Car):
    def __init__(self,battery_size=70):
        self.battery_size=battery_size
    def describe_battry(self):
        print("This car has "+str(self.battery_size)+"-kw battery.")
    def get_range(self):
        if self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=270
        message="This car can go approximately "+str(range)
        message+=" miles on a full charge."
        print(message)

#5. Python标准库
from collections import OrderedDict
favorite_languages=OrderedDict()
favorite_languages['jen']='python'
favorite_languages['sarah']='c'
favorite_languages['eward']='ruby'
favorite_languages['phil']='python'
for name,language in favorite_languages.items():
    print(name.title()+"'s favorite language is "+language.title()+".")

#6. 类编码风格
#类名用驼峰命名法，即每个单词的首字母大写而不使用下划线
#实例名和模块名都用小写，单词之间加上下划线
#每个类，均需在类定义后面包含一个文档字符串






