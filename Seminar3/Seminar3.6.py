#Напишите программу, которая просит пользователя ввести существительное, 
# и если слово введено с большой буквы, то на экран выводится сообщение "Это имя собственное.", 
# если с маленькой ‒ сообщение "Это имя нарицательное".

word = input("Введите существительное: ")

if word.istitle():
    print("Это имя собственное.")
else:
    print("Это имя нарицательное.")