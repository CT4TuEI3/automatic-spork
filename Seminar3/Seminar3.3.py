# Напишите программу, которая запрашивает у пользователя пароль, и далее:
# если пароль верный, выводит на экран сообщение "Login success".
# если пароль неверный, выводит на экран сообщение "Incorrect password, try again!" до тех пор, пока пользователь не введет верный пароль.

correctPassword = "admin"

while True:
    password = input("Введите пароль: ")

    if password == correctPassword:
        print("Login Success!")
        break
    else:
        print("Incorrect password, try again!")
    