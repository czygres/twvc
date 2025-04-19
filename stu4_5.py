# #元组
# dimensions = (200, 50)
# collection = [100, 300]
#
# print(dimensions[0])
# print(dimensions[1])
# del collection[0]
# print(str(collection) + "\n" + '--------------')
#
# print("Original dimensions: ")
# for dimension in dimensions:
#     print(dimension)
#
# dimensions = (400, 100)
# print("\nModified dimensions: ")
# for dimension in dimensions:
#     print(dimension)

# 练习
foods = ('tomato', 'ege', 'corn', 'beef', 'pig')
foods_list = [food for food in foods[:]]
print(foods_list)
