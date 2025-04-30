myVariant = 28
phoneNumber = [7, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Умножаем каждую цифру на номер варианта

multipliedList = [digit * myVariant for digit in phoneNumber]
print("Исходный список после умножения:", multipliedList)


# Разделяем на четные и нечетные через filter() + lambda

evenNumbers = list(filter(lambda x: x % 2 == 0, multipliedList))
oddNumbers = list(filter(lambda x: x % 2 != 0, multipliedList))

print("Четные элементы:", evenNumbers)
print("Нечетные элементы:", oddNumbers)
