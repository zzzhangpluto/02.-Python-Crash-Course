#1. 变量命名
message = "Hello Python world!"
print(message)


#2.字符串，用单引号/双引号均可
#2.1 改变大小写-首字母大写，全大写，全小写
name="ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
#2.2 合并
first_name="ada"
last_name="lovelace"
full_name=first_name+" "+last_name
print(full_name)
print("Hello, "+full_name.title()+"!")
#2.3添加空白
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJava")
print("Languages\n\tPython\n\tC\n\tJava")
#2.4删除空白
favorite_language=' python '
favorite_language
favorite_language.rstrip()
favorite_language=favorite_language.rstrip()
favorite_language.lstrip()
favorite_language.strip()

#2.5练习
name="Eric"
print("Hello "+name+", would you like to learn some Python today?")

famous_person="Albert Einstein"
message=famous_person+" once said,"+"'A person who never made a mistake never tried anything new.'"
print(message)

stu_name=" zz z "
print("fullname\n\t"+stu_name)
print("fullname\n\t"+stu_name.lstrip())
print("fullname\n\t"+stu_name.rstrip())


#3.数字
#3.1 整数
2+3
2-3
2*3
2/3
#乘方
2**3

#3.2 浮点数
0.2+0.1
#注意，结果的小数位数可能是不确定的
#3.3 避免类型错误
age=23
message="Happy "+str(age)+"rd Birthday!"
print(message)

#3.4 练习
print(5+3)
print(2*4)
print(9-1)
print(8/1)

love_num=1
message="my favorite number is "+str(love_num)+"!"
print(message)










