import simple_draw as sd


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


# def pentagon(point, angle=0, length=100):
#     for vector in range(5):
#         vector = sd.get_vector(start_point=point, angle=angle, length=length)
#         vector.draw()
#         angle = angle + 72
#         point = vector.end_point
#
# def hexagon(point, angle=0, length=100):
#     for vector in range(6):
#         vector = sd.get_vector(start_point=point, angle=angle, length=length)
#         vector.draw()
#         angle = angle + 60
#         point = vector.end_point
#
# def triangle(point, angle=0, length=100):
#     for vector in range(3):
#         vector = sd.get_vector(start_point=point, angle=angle, length=length)
#         vector.draw()
#         angle = angle + 120
#         point = vector.end_point
#
# def square(point, angle=0, length=100):
#     for vector in range(4):
#         vector = sd.get_vector(start_point=point, angle=angle, length=length)
#         vector.draw()
#         angle = angle + 90
#         point = vector.end_point
#
#
# point = sd.get_point(100, 350)
# pentagon(point=point, angle=10, length=100)
#
# point = sd.get_point(400, 350)
# hexagon(point=point, angle=10, length=100)
#
# point = sd.get_point(100, 150)
# triangle(point=point, angle=10, length=100)
#
# point = sd.get_point(400, 150)
# square(point=point, angle=10, length=100)

# создаем функцию с параметрами точка начала, угол наклона, радиус угла, длина и колво линий
def figure(point, angle=0, angle_l=0, length=100, number_line=1):
    for vector in range(number_line): # создает вектор из количества линий
        vector = sd.get_vector(start_point=point, angle=angle, length=length)
        vector.draw()
        angle = angle + angle_l # угол наклона + угол
        point = vector.end_point # рисует сл линию с конца предыдущей



point = sd.get_point(100, 350) # точка начала
figure(point=point, angle=10, angle_l=72, number_line=5)  # вызываем функцию

point = sd.get_point(400, 350)
figure(point=point, angle=10, angle_l=60, number_line=6)

point = sd.get_point(100, 150)
figure(point=point, angle=10, angle_l=120, number_line=3)

point = sd.get_point(400, 150)
figure(point=point, angle=10, angle_l=90, number_line=4)





# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
