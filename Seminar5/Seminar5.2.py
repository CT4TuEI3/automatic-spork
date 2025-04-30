def nums(number):
    # Возвращает список из предыдущего и следующего числа
    previousNumber = number - 1
    nextNumber = number + 1
    return [previousNumber, nextNumber]


result = nums(2025)
print(result)
