"""
Строка считается действительной, если все символы в строке встречаются одинаковое количество раз.
Также допустимо, если для выполнения этого условия будет достаточно удалить 1 символ из строки.
Напишите функцию, которая возвращает True, если строка действительна и False, если нет.
abc->True  
abcc->True
Формат ввода
abccc
Формат вывода
False
"""

def func(input):
    dictionary = [[],[]]
    for char in input:
        if char not in dictionary[0]:
            dictionary[0].append(char)
            dictionary[1].append(1)
        else:
            dictionary[1][dictionary[0].index(char)]+=1
    print(dictionary[0])
    print(dictionary[1])

    prev = dictionary[1].pop(0)
    count = 0
    for num in dictionary[1]:
        if prev != num:
            if abs(num - prev) > 1:
                return False
            elif abs(num - prev) == 1:
                count+=1
        prev = num
        
    
    if count > 1:
        return False
    else:
        return True

print("Введите строку:")
instr = input()
print("Результат: ")
print(func(instr)) 