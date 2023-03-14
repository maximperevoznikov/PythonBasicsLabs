import pandas as pd

def func(df, g, s, a):
    if a == 'count':
        res = df.groupby(g)[s].count()
    if a == 'min':
        res = df.groupby(g)[s].min()
    if a == 'max':
        res = df.groupby(g)[s].max()
    return res

dataframe = pd.read_csv("titanic.csv")
cols = list(dataframe.columns)

print("Столбцы:")
print(cols)

print("Выберете столбец для группировки:")
group = input()
if group not in cols:
    print("Ошибка: неверный ввод")
    exit()

print("Выберете столбец для обработки:")
stat = input()
if stat not in cols:
    print("Ошибка: неверный ввод")
    exit()
if stat == group:
    print("Ошибка: столбцы не должны совпадать")
    exit()

actions = ["count", "min", "max"]
print("Выберете показатель (count, min, max):")
action = input()
if action not in actions:
    print("Ошибка: неверный ввод")
    exit()

result = func(dataframe, group, stat, action)
print("")
print(result)
