my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')


print("my favorite foods are:")
for food in my_foods[:]:
	print(food.title())

print("\nMy fried's favorite foods are:")
for friend_food in friend_foods[:]:
	print(friend_food.title())
