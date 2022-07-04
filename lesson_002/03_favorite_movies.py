# РЕШЕНО

# Есть строка с перечислением фильмов
from pprint import pprint

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.
terminator = my_favorite_movies[0:10]
five_element = my_favorite_movies[12:25]
avatar = my_favorite_movies[27:33]
chyjoi = my_favorite_movies[35:40]
back = my_favorite_movies[42:57]
#
pprint(terminator)
pprint(five_element)
pprint(avatar)
pprint(chyjoi)
pprint(back)
