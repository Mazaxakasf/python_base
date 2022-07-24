import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


colors = {0: ('red', sd.COLOR_RED),
          1: ('orange', sd.COLOR_ORANGE),
          2: ('yellow', sd.COLOR_YELLOW),
          3: ('green', sd.COLOR_GREEN),
          4: ('cyan', sd.COLOR_CYAN),
          5: ('blue', sd.COLOR_BLUE),
          6: ('purple', sd.COLOR_PURPLE)}

def figure(point, angle=0, angle_l=0, length=100, i=1):
    for vector in range(i):
        vector = sd.get_vector(start_point=point, angle=angle, length=length)
        vector.draw(color=colors[color_input][0])
        angle = angle + angle_l
        point = vector.end_point

print('Возможные цвета:')
for number_color in (colors):
    print(number_color, ':', colors[number_color][0])


while True:
    color_input = input('Введите желаемый цвет')

    if color_input.isdigit():
        color_input = int(color_input)
        if color_input in colors:
            point = sd.get_point(100, 350)
            figure(point=point, angle=0, angle_l=72, i=5)

            point = sd.get_point(100, 350)
            figure(point=point, angle=0, angle_l=72, i=5)

            point = sd.get_point(400, 350)
            figure(point=point, angle=0, angle_l=60, i=6)

            point = sd.get_point(100, 150)
            figure(point=point, angle=0, angle_l=120, i=3)

            point = sd.get_point(400, 150)
            figure(point=point, angle=0, angle_l=90, i=4)
            break
        else:
            print('Не верный номер')
    else:
        print('Только цифры')






sd.pause()
