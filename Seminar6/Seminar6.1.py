myVariant = 28
multiplier = myVariant + 7
numbers = [12, 24, 36, 48, 109, 187]

def multiplyNumber(x):
    return x * multiplier


# Применяем функцию multiplyNumber через map()

resultA = list(map(multiplyNumber, numbers))
print("Способ A:", resultA)


# Используем lambda-функцию 

resultB = list(map(lambda x: x * multiplier, numbers))
print("Способ B:", resultB)