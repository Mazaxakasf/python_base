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

# создаем функцию с параметрами точка начала, угол наклона, радиус угла, длина и колво линий
def figure(point, angle=0, angle_l=0, length=100, number_line=1):
    for vector in range(number_line): # создает вектор из количества линий
        vector = sd.get_vector(start_point=point, angle=angle, length=length)
        vector.draw(color=colors[color_input][0]) # присваивает введенный цвет
        angle = angle + angle_l # угол наклона + угол
        point = vector.end_point # рисует сл линию с конца предыдущей

print('Возможные цвета:')
for number_color in colors:
    print(number_color, ':', colors[number_color][0])


while True:
    color_input = input('Введите желаемый цвет')

    if color_input.isdigit():  #проверка если будут введины другие символы
        color_input = int(color_input)
        if color_input in colors: # проверка на колство элементов в списке
            point = sd.get_point(100, 350)
            figure(point=point, angle=0, angle_l=72, number_line=5)

            point = sd.get_point(100, 350)
            figure(point=point, angle=0, angle_l=72, number_line=5)

            point = sd.get_point(400, 350)
            figure(point=point, angle=0, angle_l=60, number_line=6)

            point = sd.get_point(100, 150)
            figure(point=point, angle=0, angle_l=120, number_line=3)

            point = sd.get_point(400, 150)
            figure(point=point, angle=0, angle_l=90, number_line=4)
            break
        else:
            print('Не верный номер')
    else:
        print('Только цифры')




sd.pause()
