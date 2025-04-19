# #切片
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# for player in players[:3]:
#     print(player.title())
# # print(players[2].upper())
# print("******************************")
#
# my_food = ['pizza', 'falafel', 'carrot cake']
#
# print("My favorite foods are: ")
# print(my_food)
#
# friend_food = my_food[:]
# friend_food.append('ice cream')
# friend_food.insert(2, 'apple')
# print("\nMy friend's favorite foods are: ")
# print(friend_food)
my_food = ['pizza', 'falafel', 'carrot cake', 'banana', 'ice cream']
string_first = "The first three items in the list are : "
string_next = "Three items from the middle of the list are : "
string_end = "The last three items in the list are : "
print(string_first + str(my_food[:3]))
print(string_next + str(my_food[1:-1]))
print(string_end + str(my_food[-3:]))

pizza = my_food[:]
print("*********************" + "\n" + str(pizza))
friend_pizza = pizza[:]
pizza.append('tomato')
friend_pizza.append('potato')

my_message = [food for food in pizza[:]]
print("----------------------------------!" + "\n" + "My favorite pizza are : " + str(my_message))
my_friend_message = [food for food in friend_pizza[:]]
print("================================================!!" + "\n" +
      "My friend favorite pizza are : " + str(my_friend_message))
