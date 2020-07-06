#1.什么是列表
bycycles =['trek', 'cannondale','redline','specialized']
#1.1返回第一个元素
print(bycycles[0])
print(bycycles)
print(bycycles[0].title())

#1.2返回最后一个元素
print(bycycles[-1])

#1.3使用元素
message = "My first bycycle was a "+bycycles[0].title()+"."
print(message)

#1.4练习
names=["zzz","fs","xyh"]
print(names[0])
print(names[1])
print(names[-1])
print("hi,"+names[1])


#2. 修改、添加和删除元素
#2.1修改元素
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0]='ducati'
print(motorcycles)

#2.2添加元素
#在末尾添加
motorcycles.append('honda')
print(motorcycles)

motorcycle=[]
motorcycle.append('honda')
motorcycle.append('yamaha')
print(motorcycle)

#2.2插入元素
motorcycles.insert(0,'abc')
print(motorcycles)


#2.3删除元素
#使用del语句，删除后不可访问
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)
#使用pop()删除后最后的数但还能使用
motorcycles=['honda','yamaha','suzuki']
popped_motorcycle=motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
#弹出任何位置的元素
motorcycles=['honda','yamaha','suzuki']
first_owned=motorcycles.pop(0)
print("The first motocycle I owned was a "+first_owned.title()+".")
#根据值删除remove()，只会删除第一个指定的值，重复出现需要循环
motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
too_expensive='yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+too_expensive.title()+"is too expensive for me.")

#2.4练习
names=["zzz","fs","xyh"]
print("invitation for "+names[1])

cannot_come=names.pop(1)
print(cannot_come)

names.insert(1,'lf')
print("invitation for "+names[1])

names.append('ymw')
print(names)

names.insert(0,'xdl')
print(names)

cantgo1=names.pop(2)
cantgo2=names.pop(2)
cantgo3=names.pop(2)
cantgo4=names.pop(2)
print(names)
print("you cannot go"+cantgo1)

del names[1]
print(names)


#3. 排序列表
#3.1永久排序sort()
cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

#3.2临时排序sorted()
cars=['bmw','audi','toyota','subaru']
print("The original list is:")
print(cars)
print("The sorted list is:")
print(sorted(cars))
print("The original list again:")
print(cars)

#3.2将列表倒过来reverse()
cars=['bmw','audi','toyota','subaru']
cars.reverse()
print(cars)

#3.4确定列表长度len()
len(cars)

#3.5练习
cities=['hz','sh','bj','sz','gz']
print(cities)
print(sorted(cities))
print(cities)
print(sorted(cities,reverse=True))
print(cities)
cities.reverse()
print(cities)
cities.reverse()
print(cities)
cities.sort()
print(cities)
cities.sort(reverse=True)

names=["zzz","fs","xyh"]
len(names)


#4. 索引错误
#索引超出列表元素

