#!/usr/bin/env python
# -*- coding: utf-8 -*-

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     'nanxi': 'java'
#     }

# print("Sarah's favorite language is " + 
#     favorite_languages['sarah'].title() +
#      ".")

# for key, value in favorite_languages.items():
# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())
#     if name in friends:
#         print("Hi " + 
#         name.title() + 
#         ", I see you favorite lange is " + 
#         favorite_languages[name].title() + "!"
#         )

# for name, language in favorite_languages.items():
#     print(name, language)

# command:6-5
# author:motion
# time:10-15

River_Country = {
                'England': 'Thames',
                'Holand': 'Rhine',
                'nile': 'egypt',
                'China': 'Yangtze',
                'America': 'Mississippi',
                'Germany': 'Donau',
                }

# 钟意的河流列表
River_Prefer = ['rhine', 'thames', 'mississippi', 'Yellow Rriver']

# for river, country in River_Country.items():
#     print("\"The " + str(river).title() + "runs through " + str(country).title() + ".\"")
# item = 0

# for country in River_Country.keys():
#     item = item + 1
#     print("This is the " + str(item) + " River, Name is " + country.title())

# for river in River_Country.values():
#     print("All of The River are : %s"  % river.title())

# Tip:important contents ! ***

# for prefer in River_Prefer:
#     if prefer.title() in [river.title() for river in River_Country.values()]:
#         print("I like " + str(prefer.title()) + " Vrey March !")
#     else:
#         print(str(prefer) + " was Nice to meet .")

# 嵌套
# date time : 10-15

# 自动批量生成外星人(对象)

# 创建一个用于存储外星人的空列表
aliens = []

# 创建30个绿色外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# 显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("... " + str(len(aliens)))
