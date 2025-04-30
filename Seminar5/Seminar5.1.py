# Возвращает квадрат числа
def square(number):
    return number ** 2


# Выводит сообщение и ничего не возвращает

def printSquare(number):
    squareValue = number ** 2
    print("Квадрат числа равен: " + str(squareValue))


# Выводит сообщение и возвращает квадрат числа

def printAndReturnSquare(number):
    squareValue = number ** 2
    print("Квадрат числа равен: " + str(squareValue))
    return squareValue

result1 = square(5)
print(result1)

printSquare(5)

result3 = printAndReturnSquare(5)
print(result3)
