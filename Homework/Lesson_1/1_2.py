# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

def Cranes(number):
    if number%6!=0:
        print("Некорректное условие: количество журавликов должно быть кратно 6")
    else:
        print(f"Петя сделал {number//6} журавликов, Катя - {number//3*2}, Сережа - {number//6}")

Cranes(36)