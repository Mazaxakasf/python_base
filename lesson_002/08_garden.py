# РЕШЕНО

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
garden_set = set(garden)
meadow_set = set(meadow)
print(garden_set)
print(meadow_set)

# выведите на консоль все виды цветов
all_set = garden_set | meadow_set
print(all_set)

# выведите на консоль те, которые растут и там и там
same_set = garden_set & meadow_set
print(same_set)

# выведите на консоль те, которые растут в саду, но не растут на лугу
g_set = garden_set - meadow_set
print(g_set)

# выведите на консоль те, которые растут на лугу, но не растут в саду
m_set = meadow_set - garden_set
print(m_set)


