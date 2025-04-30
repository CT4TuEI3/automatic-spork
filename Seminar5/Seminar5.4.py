import math

def myLog(numbers):
    result = []
    for num in numbers:
        if num > 0:
            result.append(math.log(num))
        else:
            result.append(None)
    return result


inputNumbers = [1, 3, 2.5, -1, 9, 0, 2.71]
result = myLog(inputNumbers)
print(result)
