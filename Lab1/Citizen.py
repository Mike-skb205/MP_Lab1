from datetime import datetime

"""Класс, описывающий объект поезда """
class Citizen:
    """Инициализирует объект, влючает :ФИО, улицу, дом, квартиру, год рождения"""
    def __init__(self, citizen_name, street, house, kv, year):
        self.citizen_name = citizen_name
        self.street = street
        self.house = house
        self.kv = kv
        self.year = year

    """Перегрузка оператора <"""
    def __lt__(self, other):
        if self.citizen_name != other.citizen_name:
            return self.citizen_name < other.citizen_name
        if self.street != other.street:
            return self.street < other.street
        if self.kv != other.kv:
            return self.kv < other.kv
        return self.house < other.house

    """Перегрузка оператора <="""
    def __le__(self, other):
        if self.citizen_name != other.citizen_name:
            return self.citizen_name <= other.citizen_name
        if self.street != other.street:
            return self.street <= other.street
        if self.kv != other.kv:
            return self.kv <= other.kv
        return self.house <= other.house

    """Перегрузка оператора >"""
    def __gt__(self, other):
        if self.citizen_name != other.citizen_name:
            return self.citizen_name > other.citizen_name
        if self.street != other.street:
            return self.street > other.street
        if self.kv != other.kv:
            return self.kv > other.kv
        return self.house > other.house

    """Перегрузка оператора >="""
    def __ge__(self, other):
        if self.citizen_name != other.citizen_name:
            return self.citizen_name <= other.citizen_name
        if self.street != other.street:
            return self.street >= other.street
        if self.kv != other.kv:
            return self.kv >= other.kv
        return self.house >= other.house
