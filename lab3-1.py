"""
Задание 1. 
Написать программу для сжатия строки, в которой алгоритм работает следующим образом:
string = 'xxxxtttсyyaaa' преобразуется в 'x4t3с1y2a3',
то есть последовательность одинаковых символов строки заменяется на этот символ
и количество его повторений в текущей позиции строки.
Формат ввода:
xxxxtttсyyaaa
Формат вывода
x4t3с1y2a3
"""

print("Введите строку")
string = input()
#Проверка что все символы буква
if not string.isalpha():
    print("Ошибка: неправильный ввод")
else:
    dictionary = [[], []]
    #Добавить первый символ строки в словарь
    dictionary[0].append(string[0])
    dictionary[1].append(0)
    #Подсчет повторных символов
    for char in string:
        if char != dictionary[0][-1]:
            dictionary[0].append(char)
            dictionary[1].append(1)
        else:
            dictionary[1][-1]+=1
        #print(dictionary)
    #Формирование строки для вывода
    outstr = ""    
    for x in range(len(dictionary[0])):
        outstr = outstr + dictionary[0][x] + str(dictionary[1][x])
    print("Результат:" + outstr)