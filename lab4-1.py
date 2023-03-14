"""
Создайте функцию, которая принимает переменное количество аргументов и находит среднее арифметическое ненулевых из них.
Обратите внимание на формат вывода

1 2 3        --->   2  
2 0 0 2 2    --->   2  
2 0 2 1 1    --->   1.5
"""
def avg(nums):
    summ = 0
    count = 0
    for x in nums:
        if x != 0:
            summ+=x
            count+=1
    return summ / count

print("Введите числа")
string = input()
string = string.split()
print(string)
numbers = []
error = False
for x in string:
    try:
        x = float(x)
        numbers.append(x)
    except ValueError as e:
        error = True

if not error:
    print("Результат: " + str(avg(numbers)))
else:
    print("Ошибка. Направильный ввод. Вводите вещественные числа через точку. Разделяйте числа через пробел.")
