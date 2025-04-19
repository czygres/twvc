#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cars = ['audi', 'bmw', 'subaru', 'toyota']

# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# age_0 = 22
# age_1 = 19
# print(age_0 >= 21 or age_1 >= 21)

# requested_toppings = ['mushrooms', 'onions', 'pineapple']
# tof = 'mushrooms' in requested_toppings
# print(tof)

# age = 66
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# elif age < 65:
#     price = 10
# elif age >= 65:
#     price = 5
# print("Your adminssion cost is " + str(price) + '.')

# --test demo

# alien_color = ('green', 'yellow', 'red')
# alien_shoot = 'red'
# score = 0

# if alien_shoot in alien_color:
#     score = score + 5
#     print("shooting kill score: " + str(score) + " point")
# else:
#     score = score + 10
#     print("shooting score: " + str(score) + " point")

# available_toppings = ['mushrooms', 'olives', 'green peppers',
#                       'pepperoni', 'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'frensh fries', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print("Adding " + requested_topping + '.')
#     else:
#         print("Sorry, we don't have " + requested_topping + ".")

# print("\nFinished making your pizza!")

# --test 5-8

# users = ['username', 'admin', 'administator', 'cs', 'motion']
# users = []

# if not users:
#     print('"We need to find some users!"')
# else:
#     for user in users:
#         if user == 'admin':
#             print('"Hello ' + str(user) + ', would you like to see a status report?"')
#         else:
#             print('"Hello Eric, thank you for logging in again".')

# commond
# 2021-10-19
# authro:motion
#
# current_users = ['Lina', 'Alice', 'Feio', 'John', 'tom']
# new_users = ['Naci', 'Tom', 'FEio', 'Piaon', 'Jack']

# if not new_users:
#     print("We need to find some users !")
# else:
#     for user in new_users:
#         if user.lower() in [current_user.lower() for current_user in current_users]:
#             print(str(user) + " has been user, Please try again .")
#         else:
#             print(str(user) + " is OK !")

# commond 遍历数组
# author:motion

nums = list(range(1, 10))
# print(nums)
for num in nums:
    if num == 1:
        print(str(num) + 'st')
    elif num == 2:
        print(str(num) + 'nd')
    elif num == 3:
        print(str(num) + 'rd')
    else:
        print(str(num) + 'th')

