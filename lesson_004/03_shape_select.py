import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

figures = {0: 'Треугольник', 1: 'Квадрат', 2: 'Пятиугольник', 3: 'Шустиугольник'} #создаем список для выбора
point = sd.get_point(250, 300)

# создаем функцию с параметрами точка начала, угол наклона, радиус угла, длина и колво линий
def figure(point, angle=0, angle_l=0, length=100, number_line=1):
    for vector in range(number_line): # создает вектор из количества линий
        vector = sd.get_vector(start_point=point, angle=angle, length=length)
        vector.draw()
        angle = angle + angle_l # угол наклона + угол
        point = vector.end_point # рисует сл линию с конца предыдущей


print('Возможные фигуры:')
for number_figures in figures:
    print(number_figures,':', figures[number_figures]) # выводим массив

while True: #обворачиваем код, чтоб после неверного ввода спрашивало опять
    figure_input = input('Введите желаемую фигуру') # окно ввода
    if figure_input.isdigit():  # проверяем чтобы были введены только цифры
        figure_input = int(figure_input)  # переводим введенные цифры в int
        if figure_input == 0:
            figure(point=point, angle=10, angle_l=120, i=3)
            print('Вы выбрали треугольник')
            break
        elif figure_input == 1:
            figure(point=point, angle=10, angle_l=90, i=4)
            print('Вы выбрали квадрат')
            break
        elif figure_input == 2:
            figure(point=point, angle=10, angle_l=72, i=5)
            print('Вы выбрали пятиугольник')
            break
        elif figure_input == 3:
            figure(point=point, angle=10, angle_l=60, i=6)
            print('Вы выбрали шестиугольник')
            break
        else:
            print('Вы ввели не верное число')
    else:
        print('Только цифры')




sd.pause()
