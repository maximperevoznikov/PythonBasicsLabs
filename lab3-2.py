"""
Для строки вывести статистику по количеству входящих в нее символов (без учета регистра), сортируя по алфавиту.
Игнорируйте всё, кроме букв латиницы и кириллицы.
Вывод: символ, пробел, количество.
Приоритет вывода у латиницы, вывод символов в нижнем регистре.

Формат ввода
Hello 123 ** hello мама
Формат вывода
e 2
h 2
l 4
o 2
а 2
м 2
"""
print("Введите строку")
string = input()
cyril = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
dict=[[], []]
for c in string:
    c = c.lower()
    if c.isalpha() or c in cyril:
        if c not in dict[0]:
            dict[0].append(c)
            dict[1].append(1)
        else:
            i = dict[0].index(c)
            dict[1][i]+=1 
newdict=[]
for x in range(len(dict[0])):
    newdict.append([dict[0][x], dict[1][x]])
    newdict.sort()
for x in newdict:
    #print(newdict[x])
    print(x[0] + ' ' + str(x[1]))
