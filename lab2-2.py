num = -1
while num < 0:
    print("Введите индекс числа Фибоначчи (начиная с 0): ")
    try:
        num = int(input())
    except ValueError as e:
        print('Это не число')
    

a = 1
b = 0
for x in range(num):
    a += b
    b = a - b
print("Число Фибоначчи с индексом", num, '=', b)