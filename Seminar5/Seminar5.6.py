#Вычисляет биномиальный коэффициент C(n, k)

def binomCoeff(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)  #Cимметрия
    result = 1
    for i in range(1, k + 1):
        result = result * (n - k + i) // i
    return result


#Вычисляет вероятность получить ровно k успехов в n испытаниях Бернулли

def binomProb(p, n, k):
    if p < 0 or p > 1:
        raise ValueError("Вероятность p должна быть в диапазоне [0, 1]")
    if k < 0 or k > n:
        return 0.0
    
    combination = binomCoeff(n, k)
    probability = combination * (p ** k) * ((1 - p) ** (n - k))
    return probability


print(binomProb(0.3, 5, 0))  # Вероятность 0 успехов
print(binomProb(0.7, 8, 8))  # Вероятность 8 успехов из 8
print(binomProb(0.4, 10, 11))  # Невозможный случай: 0.0

