# НЕ РЕШЕНО!!!

# (цикл for)
import simple_draw as sd
sd.resolution = (1200, 600)
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
left_bottom_x, left_bottom_y = 0, 0
right_top_x, right_top_y = 100, 50

for y in range(50, 610, 50):
    for x in range(0, 1210, 100):
        # point = sd.get_point(x, 0)
        left_bottom = sd.get_point(left_bottom_x, left_bottom_y)
        right_top = sd.get_point(x, y)
        sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=1)


sd.pause()
