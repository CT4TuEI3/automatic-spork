import math

#Напишите программу, которая принимает на вход список L, в котором хранятся значения доходов домохозяйств за месяц,
# а возвращает новый список L2 ‒ список логарифмированных значений доходов.

def logMethod(incomes):
    return [math.log(income) for income in incomes]

incomes = [100, 120, 125, 175, 200]
print(logMethod(incomes))
