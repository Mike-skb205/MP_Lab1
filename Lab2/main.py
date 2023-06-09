## Main
#  Here are all functions called

import random
import pandas as pd
import timeit

import numpy as np
import matplotlib.pyplot as plt

from find_algorithms import simple_search
from find_algorithms import binary_search
from find_algorithms import heap_sort
from collections import defaultdict
from Citizen import Citizen

"""Размерность сгенерированных наборов данных"""
nums = [101, 200, 440, 1000, 5000, 50000, 105000]

"""Чтение из файла и запись в словарь, для дальнейшей сортировки"""
citizens = {}
for i in nums:
    curr = pd.read_excel('./citizens_sorted_pyramid.xlsx', sheet_name=f'{i}').to_dict('records')
    curr_citizens = []
    for citizen in curr:
        curr_citizens.append(Citizen(citizen['ФИО'], citizen['Улица'],
                                     citizen['Дом'], citizen['Квартира'], citizen['Год рождения'])
        )

    citizens[i] = curr_citizens

"""Списки для хранения времени, потраченного на сортировку"""
time_spent_simple = []
time_spent_binary_sort = []
time_spent_binary = []
time_spent_key = []

for j in nums:
    names = [k.citizen_name for k in citizens[j]]
    key = Citizen(random.choice(names), "", "", "", "")
    citizen_multi_map = defaultdict(list)
    for citizen in citizens[j]:
        citizen_multi_map[citizen.citizen_name].append(citizen)

    """Поиск по ключу в массиве"""
    starttime_1 = timeit.default_timer()
    print(citizen_multi_map[key.citizen_name])
    end_1 = timeit.default_timer() - starttime_1
    time_spent_key.append(end_1)

    """Простой поиск"""
    starttime_2 = timeit.default_timer()
    simple_search(citizens[j], key)
    end_2 = timeit.default_timer() - starttime_2
    time_spent_simple.append(end_2)

    """Бинарный поиск с сортировкой"""
    starttime_3 = timeit.default_timer()
    heap_sort(citizens[j])
    binary_search(citizens[j], 0, len(citizens[j]), key)
    end_3 = timeit.default_timer() - starttime_3
    time_spent_binary_sort.append(end_3)

    """Бинарный поиск"""
    starttime_4 = timeit.default_timer()
    binary_search(citizens[j], 0, len(citizens[j]), key)
    end_4 = timeit.default_timer() - starttime_4
    time_spent_binary.append(end_4)

print(f'time_spent_simple = {time_spent_simple}')
print(f'time_spent_binary_sort = {time_spent_binary_sort}')
print(f'time_spent_binary = {time_spent_binary}')
print(f'time_spent_key = {time_spent_key}')

#Отрисовка
x = [np.array(time_spent_simple), np.array(time_spent_binary),
     np.array(time_spent_binary_sort), np.array(time_spent_key)]
y = np.array(nums)
plt.plot(y, x[0], '-')
plt.plot(y, x[1], '--')
plt.plot(y, x[2], '-.')
plt.plot(y, x[3], ':')
plt.legend(['Simple search', 'Binary search',
           'Binary search(sorted)', 'Map search'])
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()