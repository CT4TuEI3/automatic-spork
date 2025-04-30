# Разбиваем строку на слова по пробелам и приводим к нижнему регистру

def strLower(inputString):
    wordsList = inputString.split(" ")
    lowerWords = [word.lower() for word in wordsList]
    return lowerWords


inputStr = "В лесу родилась ёлочка В лесу она росла"
result = strLower(inputStr)
print(result)
