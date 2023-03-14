def f1(*nums):
    summ = 0
    count = 0
    for x in nums:
        if x != 0:
            summ+=x
            count+=1
    return summ / count