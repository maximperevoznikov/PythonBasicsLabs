"""
Задание 5.
Веб-сайт требует, чтобы пользователи вводили пароль для регистрации, соответствующий определенным требованиям.
Напишите программу для проверки правильности ввода пароля пользователями.
Ниже приведены критерии проверки пароля:
1. Минимум 1 буква латинского алфавита в нижнем регистре [az]
2. Минимум 1 число от [0–9]
3. Минимум 1 буква латинского алфавита в верхнем регистре [AZ]
4. Минимум 1 специальный символ
5. Минимальная длина пароля : 6
6. Максимальная длина пароля: 12
Программа должна возвращать True или False.
Формат ввода
Passw1#0rd
Формат вывода
True
"""

def func(str):
    special = "!@#$%^&*()!№;%:?*"
    check1 = False
    check2 = False
    check3 = False
    check4 = False
    check5 = False
    check6 = False
    for char in str:
        if char.isdigit():
            check1 = True
        if char.islower():
            check2 = True
        if char.isupper():
            check3 = True
        if special.find(char) != -1:
            check4 = True
    if len(str) >= 6:
        check5 = True
    if len(str) <= 12:
        check6 = True
    print("Проверка на число")
    print(check1)
    print("Проверка на нижний регистр")
    print(check2)
    print("Проверка на верхний регистр")
    print(check3)
    print("Проверка на спец. символ")
    print(check4)
    print("Проверка на мин длину 6")
    print(check5)
    print("Проверка на макс длину 12")
    print(check6)
    print("Результат: ")
    return check1 and check2 and check3 and check4 and check5 and check6

print("Введите строку:")
instr = input()
print(func(instr))  
    