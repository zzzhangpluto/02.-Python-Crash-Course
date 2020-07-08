#1. 简单字典
alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

#2. 使用字典：键-值对
#2.1访问字典中的值
alien_0={'color':'green'}
print(alien_0['color'])

alien_0={'color':'green','points':5}
new_points=alien_0['points']
print("You just earned "+str(new_points)+" points!")

#2.2添加键-值对
alien_0={'color':'green','points':5}
print(alien_0)
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)
#添加顺序无所谓，只关心键与值的对应关系

#2.3先创建一个空字典
alien_0={}
alien_0['color']='green'
alien_0['points']=5
print(alien_0)

#2.4修改字典中的值
alien_0={'color':'green'}
print("The alien is "+alien_0['color']+".")
alien_0['color']='yellow'
print("The alien is now "+alien_0['color']+".")

alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print("Original x-position: "+str(alien_0['x_position']))
#向右移动外星人
#据外星人当前速度决定将其移动多远
if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    x_increment=3
#新位置等于老位置加上增量
alien_0['x_position']=alien_0['x_position']+x_increment
print("New x-position: "+str(alien_0['x_position']))

#2.5删除键-值对
alien_0={'color':'green','points':5}
print(alien_0)
del alien_0['points']
print(alien_0)

#2.6由类似对象组成的字典
favorite_languages={'jen':'python',
                    'sarah':'c',
                    'eward':'ruby',
                    'phil':'python'
                    }
favorite_languages['sarah']

#2.7练习
personal_info={'first_name':'abc','last_name':'def','age':13,'city':'hz'}
print(personal_info['first_name'])
print(personal_info['last_name'])
print(personal_info['age'])
print(personal_info['city'])

#3. 遍历字典
#3.1遍历所有的键-值对
user_0={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}

for key, value in user_0.items():
    print("\nKey: "+key)
    print("Value: "+value)

favorite_languages={'jen':'python',
                    'sarah':'c',
                    'eward':'ruby',
                    'phil':'python'
                    }
for name, language in favorite_languages.items():
    print(name.title()+"'s favorite language is "+language.title()+".")

#3.2遍历字典中所有键
favorite_languages={'jen':'python',
                    'sarah':'c',
                    'eward':'ruby',
                    'phil':'python'
                    }
for name in favorite_languages.keys():
    print(name.title())

friends=['phil','sarah']
for name in favorite_languages.keys():
    if name in friends:
        print(" Hi "+name.title()+", I see your favorite language is "+favorite_languages[name].title()+"!")

if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!')

#3.3按顺序遍历字典中的所有键
favorite_languages={'jen':'python',
                    'sarah':'c',
                    'eward':'ruby',
                    'phil':'python'
                    }
for name in sorted(favorite_languages.key()):
    print(name.title()+", thank you for taking the poll.")

#3.4遍历字典中的所有值
favorite_languages={'jen':'python',
                    'sarah':'c',
                    'eward':'ruby',
                    'phil':'python'
                    }
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
#如果要剔除重复项
favorite_languages={'jen':'python',
                    'sarah':'c',
                    'eward':'ruby',
                    'phil':'python'
                    }
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

#4. 嵌套
#4.1字典列表
alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}
aliens={alien_0,alien_1,alien_2}
for alien in aliens:
    print(alien)

aliens=[]
for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of aliens: "+str(len(aliens)))

aliens=[]
for alien_number in range(0,30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10
for alien in aliens[0:5]:
    print(alien)
print("...")

for alien in aliens[0:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10
    elif alien['color']=='yellow':
        alien['color']='red'
        alien['speed']='fast'
        alien['points']=15

#4.2在字典中存储列表
pizza={
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
    }
print("You ordered a "+pizza['crust']+"-crust pizza"+
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t"+topping)

#4.3在字典中存储字典
users={
    'asinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
}
for username,user_info in users.items():
    print("\nUsername: "+username)
    full_name=user_info['first']+user_info['last']
    location=user_info['location']
    print("\tFull name: "+full_name.title())
    print("\tLocation: "+location.title())




