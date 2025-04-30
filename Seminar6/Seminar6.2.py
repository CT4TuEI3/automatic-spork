myPhone = [7, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]  
otherPhone = [7, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2]  


# Умножение элементов через map() и lambda

result = list(map(lambda x, y: x * y, myPhone, otherPhone))  

print("Результат умножения:", result)  
