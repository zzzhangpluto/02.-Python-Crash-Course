#1. CSV文件格式
#1.1分析CSV文件头
import csv
filename='sitka.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    print(header_row)

#1.2打印文件头及其位置
filename='sitka.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    for index,column_header in enumerate(header_row):
        print(index,column_header)

#1.3提取并读取数据
filename='sitka.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    highs=[]
    for row in reader:
        high=int(row[1])
        highs.append(high)
    print(highs)

#1.4绘制气温图表
from matplotlib import pyplot as plt
filename='sitka.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    highs=[]
    for row in reader:
        high=int(row[1])
        highs.append(high)
    print(highs)
fig=plt.figure(dpi=128, figsize=(10,6))
plt.plot(high,c='red')
plt.title("Daily high temperatures, July 2014",fontsize=24)
plt.xlabel('',fontsize=16)
plt.ylabel("Temperature",fontsize=16)
plt.tick_params(axis='both',which='major',fontsize=16)
plt.show()

#1.5模块datetime
from datetime import datetime
first_date=datetime.strptime('2014-7-1','%Y-%m-%d')
print(first_date)
#datetime中的实参
#%A 星期几，%B 月份名，%m 用数字表示的月份，%d 用数字表示的月份中某天
#%Y 四位的年份，%y 两位的年份，%H 24小时制的小时数，%I 12小时的小时数
#%p am或pm，%M 分钟数，%S 秒数

#1.6在图表中添加日期
filename='sitka.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    dates,highs=[],[]
    for row in reader:
        current_date=datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_date)
        high=int(row[1])
        highs.append(high)
fig=plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs,c='red')
plt.title("Daily high temperatures, July 2014",fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()#避免彼此重叠
plt.ylabel("Temperature",fontsize=16)
plt.tick_params(axis='both',which='major',fontsize=16)
plt.show()

#1.7涵盖更多的时间
filename='sitka.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    dates,highs=[],[]
    for row in reader:
        current_date=datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_date)
        high=int(row[1])
        highs.append(high)
fig=plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs,c='red')
plt.title("Daily high temperatures - 2014",fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()#避免彼此重叠
plt.ylabel("Temperature",fontsize=16)
plt.tick_params(axis='both',which='major',fontsize=16)
plt.show()

#1.8再绘制一个数据系列
filename='sitka.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    dates,highs,lows=[],[],[]
    for row in reader:
        current_date=datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_date)
        high=int(row[1])
        highs.append(high)
        low=int(row[3])
        lows.append(low)
fig=plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates,highs,c='red')
plt.plot(dates,lows,c='blue')
plt.title("Daily high and low temperatures 2014",fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()#避免彼此重叠
plt.ylabel("Temperature",fontsize=16)
plt.tick_params(axis='both',which='major',fontsize=16)
plt.show()

#1.9给图表区域着色
filename='sitka.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    dates,highs,lows=[],[],[]
    for row in reader:
        current_date=datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_date)
        high=int(row[1])
        highs.append(high)
        low=int(row[3])
        lows.append(low)
fig=plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
plt.title("Daily high and low temperatures 2014",fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()#避免彼此重叠
plt.ylabel("Temperature",fontsize=16)
plt.tick_params(axis='both',which='major',fontsize=16)
plt.show()

#2. 制作交易收盘价走势图：JSON格式
#2.1下载收盘价数据
from urllib.request import urlopen
import json
json_url='https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
response=urlopen(json_url)
req=response.read()
with open('btc_close_2017_urllib.json','wb') as f:
    f.write(req)
file_urllib=json.loads(req)
print(file_urllib)

#2.2提取相关的数据
filename='btc_close_2017_urllib.json'
with open(filename) as f:
    btc_data=json.load(f)
for btc_dict in btc_data:
    date=btc_dict['date']
    month=btc_dict['month']
    week=btc_dict['week']
    weekday=btc_dict['weekday']
    close=btc_dict['close']
    print("{} is month {} week {}, weekday {}, the close price is {} RMB".format(date,month,week,weekday,close))

#2.3将字符串转换为数字值
for btc_dict in btc_data:
    date=int(btc_dict['date'])
    month=int(btc_dict['month'])
    week=int(btc_dict['week'])
    weekday=btc_dict['weekday']
    close=int(float(btc_dict['close']))#这里直接用int会报错，因为price有小数
    print("{} is month {} week {}, weekday {}, the close price is {} RMB".format(date,month,week,weekday,close))

#2.4绘制收盘价折线图
dates=[]
months=[]
weeks=[]
weekdays=[]
close=[]
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))
import pygal
line_chart=pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
line_chart.title='Close Price'
line_chart.x_labels=dates
N=20#x轴坐标每隔20天显示一次
line_chart._x_labels_major=dates[::N]
line_chart.add('Close Price',close)
line_chart.render_to_file('Close price line plot.svg')

#2.5时间序列特征初探
import math
import pygal
line_chart=pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
line_chart.title='Log Transformation of Close Price'
line_chart.x_labels=dates
N=20#x轴坐标每隔20天显示一次
line_chart._x_labels_major=dates[::N]
close_log=[math.log10(_) for _ in close]
line_chart.add('Close Price',close_log)
line_chart.render_to_file('Log transformation of close price line plot.svg')

#2.6收盘价均值
from itertools import groupby
def draw_line(x_data,y_data,title,y_legend):

    xy_map=[]
    for x,y in groupby(sorted(zip(x_data,y_data)),key=lambda _:_[0]):
        y_list=[v for _, v in y]
        xy_map.append([x,sum(y_list)/len(y_list)])
    x_unique,y_mean=[*zip(*xy_map)]
    line_chart=pygal.Line()
    line_chart.title=title
    line_chart.x_labels=x_unique
    line_chart.add(y_legend,y_mean)
    line_chart.render_to_file(title+'.svg')
    return line_chart

idx_month=dates.index('2017-12-01')
line_chart_month=draw_line(months[:idx_month],close[:idx_month],'close price monthly daily mean','monthly daily mean')
line_chart_month

idx_week=dates.index('2017-12-11')
line_chart_week=draw_line(weeks[:idx_week],close[:idx_week],'close price weekly daily mean','weekly daily mean')
line_chart_week
wd=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
weekdays_int=[wd.index(w)+1 for w in weekdays[1:idx_week]]
line_chart_weekday=draw_line(weekdays_int,close[1:idx_week],'close price week mean','week mean')
line_chart_weekday.x_labels=wd
line_chart_weekday.render_to_file('close price weekly daily mean.svg')

#2.7收盘价数据仪表盘
with open('close price dashboard.html','w',encoding='utf8') as html_file:
    html_file.write('<html><head><title>close price dashboard</title>meta charset="utf-8"></head><body>\n')
    for svg in ['Close price line plot.svg','Log transformation of close price line plot.svg',
                'close price monthly daily mean', 'monthly daily mean', 'close price weekly daily mean'
                'close price week mean']:
        html_file.write('    <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))
        html_file.write('</body></html>')
