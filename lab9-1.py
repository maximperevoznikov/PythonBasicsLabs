"""
Дан файл "titanic.csv" в формате .csv, который можно открыть командой pd.read_csv("titanic.csv")
Каждая строка набора данных - это отдельный человек, который либо выжил, либо не выжил (столбец "Survived").
В данной задаче необходимо определить количество людей в наборе данных возраст которых строго больше N.
Где N - некое целое число от 0 до 100, которое подается на вход вашей функции.
На выходе ожидается также целое число - количество пассажиров Титаника.
Формат ввода
60
Формат вывода
22
"""
import pandas as pd

def func(df, n):
    res = df[df["Age"] > n].shape[0]
    return res

dataframe = pd.read_csv("titanic.csv")
print("Введите возраст:")
age = input()

try:
    age = int(age)
    res = func(dataframe, age)
    print("Количество человек:")
    print(res)
except ValueError as e:
    print("Ошибка: неверный ввод")
    