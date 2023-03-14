"""
Напишите функцию, которая возвращает самую длинную неповторяющуюся подстроку для входной строки.
Если несколько подстрок совпадают по длине, функция возвращает ту, которая встречается первой.
xxxxx -> x  
abcdefa -> abcdef
Формат ввода
abcabcbb
Формат вывода
abc
"""
def func(string):
    substr = ""
    newsubstr = ""
    for char in string:
        if char != newsubstr[:1]:
            newsubstr+=char
        else:
            if newsubstr > substr:
                substr = newsubstr
            newsubstr = ""
            newsubstr+=char
    return substr

print("Введите строку:")
instr = input()
print("Результат: ")
print(func(instr)) 