# Вывод n-ного числа Фибоначчи через рекурсию
def FibRec(n):
    if n==1 or n==2:
        return 1
    return FibRec(n-1)+FibRec(n-2)
print(FibRec(6))