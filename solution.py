import math

"""
функция, которая принимает на вход список целых чисел и возвращает 
новый список, содержащий только уникальные элементы из исходного списка.
"""


def unique_numbs(input):
    return list(set(input))


"""
функция, которая принимает на вход два целых числа (минимум и максимум)
и возвращает список всех простых чисел в заданном диапазоне.
"""


def primes_in_range(min, max):
    def is_prime(num):
        """
        вспомогательная функция, которая определяет простое ли число,
        перебором делителей до наибольшего корня из числа
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    for num in range(min, max):
        if is_prime(num):
            primes.append(num)
    return primes


"""
класс Point, который представляет собой точку в двумерном пространстве.
Класс имеет методы для инициализации координат точки, вычисления расстояния до другой точки,
а также для получения и изменения координат.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, point):
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)

    def get_coordinates(self):
        return self.x, self.y

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y


"""
функция, которая сортирует список строк по длине, сначала по возрастанию, а затем по убыванию.
"""


def sort_by_len(input):
    asc_list = input.sort(key=len)
    desc_list = input.sort(key=len, reversed=True)
    return asc_list, desc_list
