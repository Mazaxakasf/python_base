# РЕШЕНО

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 179, 37
while a > b:  # пока 179 больше чем 37, делаем
    a -= b  # от 179 оттнимаем 37
    print(a)  #остаток от 179 после итерации
    #когда остаток от 179 меньше 37 то выходим из цикла
print('Остаток от деления: ', a)
