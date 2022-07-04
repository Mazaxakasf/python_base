# РЕШЕНО

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
from pprint import pprint

my_family = ['Отец','Мать','Брат']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['Вася', 170],['Люда', 160],['Петя', 140]
]


growth_father = my_family_height[0][1]
growth_mother = my_family_height[1][1]
growth_brother = my_family_height[2][1]


# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
pprint("Рост отца = %d" %(growth_father))
sum_age = growth_father + growth_mother + growth_brother
general_age = (growth_father + growth_mother + growth_brother) / 3
pprint("Сумма ростов моей семьи = %d"%(sum_age))
pprint("Общий рост моей семьи = %d"%(general_age.__round__()))
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
