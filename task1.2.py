from random import sample
from datetime import time
from decimal import Decimal, ROUND_HALF_DOWN


# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

import random
three_songs = random.sample(my_favorite_songs,3)
total = 0
for i in three_songs:
    total += i[1]
print('Три песни звучат', total, 'минут')



# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
print('Три песни звучат', (my_favorite_songs_dict.get(random.choice(list(my_favorite_songs_dict))))
       + (my_favorite_songs_dict.get(random.choice(list(my_favorite_songs_dict)))) + 
       (my_favorite_songs_dict.get(random.choice(list(my_favorite_songs_dict)))), 'минут')

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

import random
some_song = random.choice(list(my_favorite_songs_dict))
print(some_song)

some_another_song = random.choice(my_favorite_songs)
print(some_another_song)

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 
import datetime


