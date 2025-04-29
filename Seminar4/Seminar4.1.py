# Исходный словарь
rept = {
    "python": "питон",
    "anaconda": "анаконда",
    "tortoize": "черепаха"
}

# 1. Добавляем пару "snake" - "змея"
rept["snake"] = "змея"

# 2. Исправляем ключ "tortoize" на "tortoise"
rept["tortoise"] = rept.pop("tortoize")

# 3. Выводим сообщения для каждого слова
for eng, rus in rept.items():
    print(f"{rus.capitalize()} по-английски будет {eng}.")