# РЕШЕНО

# (определение функций)
import simple_draw as sd
sd.resolution = (1200, 600)
# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def smile(point_x, point_y):
    radius = 50
    point = sd.get_point(point_x, point_y)
    eye_l = sd.get_point(point_x - 10, point_y + 10)  # левый глаз
    eye_r = sd.get_point(point_x + 10, point_y + 10)  # правый глаз
    start_point = sd.get_point(point_x - 10, point_y - 10)   #рот
    end_point = sd.get_point(point_x + 10, point_y - 10)    #рот
    sd.circle(center_position=point, radius=radius, width=2)
    sd.circle(center_position=eye_l, radius=10, width=2)
    sd.circle(center_position=eye_r, radius=10, width=2)
    sd.line(start_point=start_point, end_point=end_point, width=2)

# делаем 10 смайликов в рандомных местах
for _ in range(10):
    r_point = sd.random_point()
    smile(r_point.x, r_point.y)



sd.pause()
