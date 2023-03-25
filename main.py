import copy
import time
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt

from Citizen import Citizen
from My_sortes import shaker_sort
from My_sortes import heap_sort
from My_sortes import insert_sort

def graphics(time, str):
    # data to be plotted
    x = np.array(time)
    y = np.array(nums)

    # plotting
    plt.title(str)
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.plot(x, y, color="green")
    plt.show()

"""Размерность сгенерированных наборов данных"""
nums = [101, 200, 440, 1000, 5000, 50000, 105000]

"""Чтение из файла и запись в словарь, для дальнейшей сортировки"""
citizens = {}
for i in nums:
    curr = pd.read_excel('./Data_1.xlsx', sheet_name=f'{i}').to_dict('records')
    curr_citizens = []
    for citizen in curr:
        curr_citizens.append(Citizen(citizen['Фио'], citizen['Улица'],
                                     citizen['Дом'], citizen['Номер кв'], citizen['Год рождения'])
        )

    citizens[i] = curr_citizens

"""Списки для хранения времени, потраченного на сортировку"""
time_spend_insert = []
time_spend_shaker = []
time_spend_pyramid = []


"""Сортировка данных, прочитанных из файла"""
for j in nums:
    sorted_arrays = []

    sorted_arr_insert = copy.deepcopy(citizens[j])
    start = time.time()
    insert_sort(sorted_arr_insert)
    end = time.time() - start
    time_spend_insert.append(end)
    sorted_arrays.append(sorted_arr_insert)

    sorted_arr_insert = copy.deepcopy(citizens[j])
    start = time.time()
    shaker_sort(sorted_arr_insert)
    end = time.time() - start
    time_spend_shaker.append(end)
    sorted_arrays.append(sorted_arr_insert)

    sorted_arr_insert = copy.deepcopy(citizens[j])
    start = time.time()
    heap_sort(sorted_arr_insert)
    end = time.time() - start
    time_spend_pyramid.append(end)
    sorted_arrays.append(sorted_arr_insert)

    for i in range(len(sorted_arrays)):
        final_dict = {}
        citizen_name = []
        street = []
        house = []
        kv = []
        year = []

        for t in sorted_arrays[i]:
            citizen_name.append(t.citizen_name)
            street.append(t.street)
            house.append(t.house)
            kv.append(t.kv)
            year.append(t.year)
        final_dict['ФИО'] = citizen_name
        final_dict['Улица'] = street
        final_dict['Дом'] = house
        final_dict['Квартира'] = kv
        final_dict['Год рождения'] = year

        """Запись в разные файлы в зависимости от метода сортировки"""
        if i == 0:
            file_name = "./citizens_sorted_insert.xlsx"
        if i == 1:
            file_name = "./citizens_sorted_shaker.xlsx"
        if i == 2:
            file_name = "./citizens_sorted_pyramid.xlsx"

        """Если это первый набор данных, создаем файл, если нет - дописываем с сущетвующий"""
        if j == 101:
            mode = 'w'
        else:
            mode = 'a'
        with pd.ExcelWriter(file_name, engine="openpyxl", mode=mode) as writer:
            pd.DataFrame(final_dict).to_excel(writer, sheet_name=f"{j}", index=False)

print(f'insert_time = {time_spend_insert}')
print(f'shaker_time = {time_spend_shaker}')
print(f'heap_time = {time_spend_pyramid}')

graphics(time_spend_insert, "Insert")
graphics(time_spend_shaker, "Shaker")
graphics(time_spend_pyramid, "Heap")