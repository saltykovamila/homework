# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'
print(type(my_favorite_songs))
print(len(my_favorite_songs))


# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

print(f"{my_favorite_songs[0:14:]}\n"
    f"{my_favorite_songs[-13:]}\n"
    f"{my_favorite_songs[16:30:]}\n"
    f"{my_favorite_songs[-26:-15:]}\n")

