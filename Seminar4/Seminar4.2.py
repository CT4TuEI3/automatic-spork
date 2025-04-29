cnt = ["Andorra", "Belarus", "Denmark", "Kenya", "Jamaica", "Romania"]
fh = [1.0, 6.0, 1.0, 4.0, 2.5, 2.0]

# Создаем словарь с помощью zip()
freedomIndex = dict(zip(cnt, fh))

print(freedomIndex)