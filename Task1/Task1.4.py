#4.1

massFirst = float(input("Введите массу первого ингредиента в граммах: "))
massSecond = float(input("Введите массу второго ингредиента в граммах: "))
massThird = float(input("Введите массу третьего ингредиента в граммах: "))

# перевод в килограммы

massFirstKg = massFirst / 1000
massSecondKg = massSecond / 1000
massThirdKg = massThird / 1000

recipeFirst = """
Рецепт

политическая теория : %.3f кг
история политических учений : %.3f кг
математика : %.3f кг

Приправить политической историей. Добавить математические модели по вкусу.
""" % (massFirstKg, massSecondKg, massThirdKg)

print(recipeFirst)


#4.2

massFirst = float(input("Введите массу первого ингредиента в граммах: "))
massSecond = float(input("Введите массу второго ингредиента в граммах: "))
massThird = float(input("Введите массу третьего ингредиента в граммах: "))

# перевод в килогграммы

massFirstKg = massFirst / 1000
massSecondKg = massSecond / 1000
massThirdKg = massThird / 1000

recipeSecond = """
Рецепт

политическая теория : {:.3f} кг
история политических учений : {:.3f} кг
математика : {:.3f} кг

Приправить политической историей. Добавить математические модели по вкусу.
""".format(massFirstKg, massSecondKg, massThirdKg)

print(recipeSecond)