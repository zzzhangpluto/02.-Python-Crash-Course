#1. 遍历列表
magicians=['alice','david','carolina']
for magician in magicians:
    print(magician)

for magician in magicians:
    print(magician.title()+", that was a great trick!")

for magician in magicians:
    print(magician.title()+", that was a great trick!")
print("Thank you, everyone.")


#2. 避免缩进错误
pizzas=['a','b','c']
for pizza in pizzas:
    print("I like"+pizza+" pizza")

#3. 创建数值列表
#3.1使用range()
for value in range(1,5):
    print(value)

#3.2使用range()创建数字列表
numbers=list(range(1,6))
print(numbers)

even_numbers=list(range(2,11,2))
print(even_numbers)

squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)

squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)

#3.3简单统计计算
digits=[1,2,3,4,5,6,7,8,9,0]
min(digits)
max(digits)
sum(digits)

#3.4列表解析
squares=[value**2 for value in range(1,11)]
print(squares)

#3.5练习
for value in range(1,21):
    print(value)

number=list(range(1,1000001))
min(number)
max(number)
sum(number)

for value in range(1,20,2):
    print(value)

for value in range(3,30,3):
    print(value)

cubes=[]
for value in range(1,11):
    cube=value**3
    cubes.append(cube)
    print(cube)
print(cubes)

cubes=[value**3 for value in range(1,11)]
print(cubes)

#4. 切片
#4.1简单切片
players=['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[:4])
print(players[2:])
#最后三个元素
print(players[-3:])

#4.2遍历切片
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

#4.3复制列表
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]
print("my favorite foods areL")
print(my_foods)
print("\nmy friend's favorite foods are")
print(friend_foods)
#注意，简单相等会导致同时操作两个列表
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)

#5. 元组--不可变的列表
#5.1定义元组
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
#试图修改就会报错
dimensions[0]=250

#5.2遍历元组中的所有值
dimensions=(200,50)
for dimension in dimensions:
    print(dimension)

#5.3修改元组变量
#不能修改元素但是能给存储元组的变量赋值
dimensions=(200,50)
print("original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions=(400,100)
print(("\nmodified dimensions:"))
for dimension in dimensions:
    print(dimension)

#6. 设置代码格式
#6.1格式设置指南PEP
#6.2缩进：建议每级缩进使用4个空格，最好不要tab和空格混用
#6.3行长：每行不超过80字符
#6.4空行：将代码各部分分开







