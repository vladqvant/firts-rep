my_foods = ['пицца', 'сыр', 'рыба']
friend_foods = my_foods[:]
my_foods.append('суши')
friend_foods.append('сырники')
for my in my_foods:
    print('Я люблю:')
    print(my)
for friend in friend_foods:
    print('Мой друг любит:')
    print(friend)