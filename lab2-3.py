summ = 10
numstr = -1
while(numstr < 0):
    print("Введите числовую строку")
    try:
        numstr = int(input())
    except ValueError as e:
        print("Строка не числовая")

while(summ >= 10):
    summ = 0
    while(numstr >= 10):
        summ += numstr%10
        numstr = int(numstr/10)
    summ += numstr
    numstr = summ
    print("Сумма чисел в строке =", summ)
print("Результирующее число =", summ)