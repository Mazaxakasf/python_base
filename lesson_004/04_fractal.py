# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения
root_point = sd.get_point(300, 30)

# создаем функцию точка рисования, угол, длинна, отклонение угла
def draw_branches(point, angle, length, delta):
    if length < 10:
        return
    draw_bunches = sd.get_vector(start_point=point, angle=angle, length=length)
    draw_bunches.draw()

    random_length = sd.random_number(70, 85) / 100 # рандомная длинна
    random_delta = sd.random_number(10, 30) # рандомный угол отклонения

    next_point = draw_bunches.end_point
    next_angle = angle - delta
    next_length = length * random_length
    #вызываем 2 ветви в разные стороны
    draw_branches(point=next_point, angle=next_angle, length=next_length, delta=random_delta)
    next_angle = angle + delta
    draw_branches(point=next_point, angle=next_angle, length=next_length, delta=random_delta)



draw_branches(point=root_point, angle=90, length=100, delta=30)
# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


