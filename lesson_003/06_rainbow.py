# РЕШЕНО

# (цикл for)

import simple_draw as sd
sd.resolution = (1200, 600)
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# start_x, start_y = 50, 50
# end_x, end_y = 350, 450
#
# for color_line in rainbow_colors:
#     start_point = sd.get_point(start_x, start_y)
#     end_point = sd.get_point(end_x, end_y)
#     sd.line(start_point=start_point, end_point=end_point, color=color_line, width=6)
#     start_x += 5
#     end_x += 5


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
point = sd.get_point(1100, -200)
radius = 800
for color_line in rainbow_colors:
    radius += 5
    sd.circle(center_position=point, radius=radius, color=color_line)

sd.pause()
