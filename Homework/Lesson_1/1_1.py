# Задача 2: Найдите сумму цифр трехзначного числа.
def DigitSum(number):
    return number%10 + (number//10)%10 + (number//100)
print(DigitSum(356))