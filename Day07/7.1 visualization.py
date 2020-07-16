#1. 绘制简单的折线图
import matplotlib.pyplot as plt
squares=[1,4,9,16,25]
plt.plot(squares)
plt.show()

#2.1修改标签文字和线条粗细
squares=[1,4,9,16,25]
plt.plot(squares,linewidth=5)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.tick_params(axis='both',labelsize=14)
plt.show()
#当只提供一系列数字时，plot()假设第一个数据点对应的x坐标是0

#2.2校正图形
input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]
plt.plot(input_values,squares,linewidth=5)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.tick_params(axis='both',labelsize=14)
plt.show()

#2.3使用scatter()绘制散点图
plt.scatter(2,4,s=200)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)
plt.show()

#2.4使用scatter()绘制一系列电
x_values=[1,2,3,4,5]
y_values=[1,4,9,16,25]
plt.scatter(x_values,y_values,s=100)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)
plt.show()

#2.5自动计算数据
x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]
plt.scatter(x_values,y_values,s=40)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)
plt.axis([0,1100,0,1100000])
plt.show()

#2.6删除数据点的轮廓
x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]
plt.scatter(x_values,y_values,edgecolor='none',s=40)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)
plt.axis([0,1100,0,1100000])
plt.show()

#2.7自定义颜色
plt.scatter(x_values,y_values,c='red',edgecolor='none',s=40)
plt.scatter(x_values,y_values,c=(0,0,0.8),edgecolor='none',s=40)
#用RGB来定义颜色时，三个数分别代表红绿蓝分量

#2.8使用颜色映射
x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=40)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)
plt.axis([0,1100,0,1100000])
plt.show()

#2.9自动保存图表
plt.savefig('squares_plot.png',bbox_inches='tight')
#bbox_inches是将图表多余的空白区域裁减掉

#3. 随机漫步
#3.1创建RandomWalk()类
from random import choice
class RandomWalk():


    """一个生成随机漫步数据的类"""
    def __init__(self,num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points=num_points
        #所有随机漫步都始于(0,0)
        self.x_values=[0]
        self.y_values=[0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        #不断漫步，直到列表达到指定的长度
        while len(self.x_values)<self.num_points:
            #决定前进方向以及这个方向前进的距离
            x_direction=choice([1,-1])
            x_distance=choice([0,1,2,3,4])
            x_step=x_direction*x_distance
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            #拒绝原地踏步
            if x_step==0 and y_step==0:
                continue
            #计算下一个点的x和y值
            next_x=self.x_values[-1]+x_step
            next_y=self.y_values[-1]+y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)

#3.3绘制随机漫步图
rw=RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values,rw.y_values,s=15)
plt.show()

#3.4模拟多次随机漫步
while True:
    #创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw=RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()
    keep_running=input("Make another walk?(y/n): ")
    if keep_running=='n':
        break

#3.5给点着色
while True:
    #创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw=RandomWalk()
    rw.fill_walk()
    point_numbers=list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=15)
    plt.show()
    keep_running=input("Make another walk?(y/n): ")
    if keep_running=='n':
        break

#3.6重新绘制起点和终点
while True:
    #创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw=RandomWalk()
    rw.fill_walk()
    point_numbers=list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=15)
    #突出起点和终点
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)
    plt.show()
    keep_running=input("Make another walk?(y/n): ")
    if keep_running=='n':
        break

#3.7隐藏坐标轴
while True:
    #创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw=RandomWalk()
    rw.fill_walk()
    point_numbers=list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=15)
    #突出起点和终点
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)
    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    keep_running=input("Make another walk?(y/n): ")
    if keep_running=='n':
        break

#3.8增加点数
while True:
    #创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw=RandomWalk(50000)
    rw.fill_walk()
    point_numbers=list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=1)
    plt.show()
    keep_running=input("Make another walk?(y/n): ")
    if keep_running=='n':
        break

#3.9调整尺寸以适应屏幕
while True:
    #创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw=RandomWalk()
    rw.fill_walk()
    #设置绘图窗口尺寸
    plt.figure(figsize=(10,6))
    point_numbers=list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=15)
    plt.show()
    keep_running=input("Make another walk?(y/n): ")
    if keep_running=='n':
        break

#4. 使用Pygal模拟掷骰子
#4.1 创建Die类
from random import randint
class Die():
    """表示一个骰子的类"""
    def __init__(self,num_sides=6):
        """骰子默认为6面"""
        self.num_sides=num_sides
    def roll(self):
        """返回一个位于1和骰子面数之间的随机值"""
        return randint(1,self.num_sides)

#4.2掷骰子
die=Die()
results=[]
for roll_num in range(100):
    result=die.roll()
    results.append(result)
print(results)

#4.2分析结果
frequencies=[]
for value in range(1,die.num_sides+1):
    frequency=results.count(value)
    frequencies.append(frequency)
print(frequencies)

#4.3绘制直方图
import pygal
frequencies=[]
for value in range(1,die.num_sides+1):
    frequency=results.count(value)
    frequencies.append(frequency)
print(frequencies)
hist=pygal.Bar()
hist.title="Results of rolling one D6 100 times"
hist.x_labels=['1','2','3','4','5','6']
hist.x_title="Result"
hist._y_title="Frequency of Result"
hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')

#4.4同时掷两个骰子
import pygal
die_1=Die()
die_2=Die()
results=[]
for roll_num in range(1000):
    result=die_1.roll()+die_2.roll()
    results.append(result)
frequencies=[]
max_result=die_1.num_sides+die_2.num_sides

for value in range(2,die.max_result+1):
    frequency=results.count(value)
    frequencies.append(frequency)

hist=pygal.Bar()
hist.title="Results of rolling one D6 100 times"
hist.x_labels=['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title="Result"
hist._y_title="Frequency of Result"
hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')

#4.5同时掷两个面数不同的骰子
die_1=Die()
die_2=Die(10)
results=[]
for roll_num in range(50000):
    result=die_1.roll()+die_2.roll()
    results.append(result)
frequencies=[]
max_result=die_1.num_sides+die_2.num_sides

for value in range(2,die.max_result+1):
    frequency=results.count(value)
    frequencies.append(frequency)

hist=pygal.Bar()
hist.title="Results of rolling a D6 and a D10 50000 times"
hist.x_labels=['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title="Result"
hist._y_title="Frequency of Result"
hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')



