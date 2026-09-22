""" Виртуальное окружение, модули, библиотеки, фреймворки """

# 1 вид - встроенные модули
import random, time, math, sqlite3, os
print(math.pi)

# импорт маленького куска из модуля
from math import e, pi, sin, sqrt
print(e)


# 2 вид - собственные модули
from lesson4_2 import Remanga

n = Remanga("огненный кулак")
n.manga_upp()


# 3 вид - внешние модули (скачиваются с сайта PyPi)
# venv - хранилище для внешних модулей
import colorama
print(colorama.Back.BLACK, colorama.Fore.RED)
print("HI NURISLAM")
