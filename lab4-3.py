"""
Напишите функцию, которая будет возвращать самое длинное слово в предложении.
Если найдено более одного слова, то функция возвращает первое.
Формат ввода
The Tower of London was built in the 15th century
Формат вывода
century
"""

def func(string):
    words = string.split(" ")
    target = ""
    for i in words:
        if len(i) > len(target):
            target = i
    return target

print("Введите строку:")
instr = input()
print("Результат: ")
print(func(instr)) 
