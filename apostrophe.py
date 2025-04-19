print('2-3、个性化消息：')
message = "Hello Eric, would you like to learn some Python ?"
print(message)

print("2-4、调整名字的大小写： ")
name_agrs = 'alice tom'
print(name_agrs.title())    # 首字母大写
print(name_agrs.upper())    # 所有字母大写
print(name_agrs.lower())    # 所有字母小写

print("2-5、名言：")
message_l = 'Albert Einstein once said, "A person who never made a mistake never tried anything new."'
print(message_l)

print("2-6、名言2：")
famous_person = 'Albert Einstein'
famous_word = '"A person who never made a mistake never tried anything new."'
print(famous_person + famous_word)

print("2-7、剔除人名中的空白：")
names = '  Albert '
print(names)
print(names.rstrip())   # 去除右侧空白字符
print(names.lstrip())   # 去除左侧空白字符
print(names.strip())    # 去除左右两侧空白字符

print('********************************')

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles[-3].title())

