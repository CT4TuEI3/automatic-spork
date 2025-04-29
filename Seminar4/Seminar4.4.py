grades = {
    'Anna': 4, 'Bob': 3, 'Claire': 5, 'Dick': 2, 'Elena': 5,
    'Fred': 5, 'George': 4, 'Kristina': 3, 'Nick': 2,
    'Ursula': 4, 'Viktor': 5
}


# Инициализация списков для разных категорий оценок

excel = []  # отличные оценки (5)
good = []   # хорошие оценки (4)
satisf = [] # удовлетворительные оценки (3)
bad = []    # плохие оценки (2)


# Перебираем словарь и распределяем студентов по спискам

for student, grade in grades.items():
    print(f"{student}: {grade}")
    
    if grade == 5:
        excel.append(student)
    elif grade == 4:
        good.append(student)
    elif grade == 3:
        satisf.append(student)
    elif grade == 2:
        bad.append(student)

# Выводим списки студентов по категориям

print("Отличники:", excel)
print("Хорошисты:", good)
print("Удовлетворительно:", satisf)
print("Неудовлетворительно:", bad)
