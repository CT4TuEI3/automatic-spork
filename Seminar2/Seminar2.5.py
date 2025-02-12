#Напишите программу, которая принимает на вход список слов такого вида:
#    words = ["Speak ","to", "me ", "of", "Florence" ,"And ", "of", "the", "Renaissance"]
# а возвращает список
#    words_clean = ["speak", "to", "me", "of", "florence", "and", "of", "the", "renaissance"]

#Другими словами, программа убирает пробелы в словах и приводит все слова к нижнему регистру.

def theDarkSideOfTheMoon(words):
    return [word.strip().lower() for word in words]

words = ["Speak ", "to", "me ", "of", "Florence", "And ", "of", "the", "Renaissance"]
print(theDarkSideOfTheMoon(words))
