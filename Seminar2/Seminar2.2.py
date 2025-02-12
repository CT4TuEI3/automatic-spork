#Напишите программу, которая берет строку "1; 2; 3; 100" и возвращает:
#список из целых чисел
#список из чисел с плавающей точкой

numbersString = "1; 2; 3; 100"

numberArray = numbersString.split(";")

intArray = [int(num.strip()) for num in numberArray]
floatArray = [float(num.strip()) for num in numberArray]

print("Список из целых чисел:", intArray)
print("Список из чисел с плавающей точкой:", floatArray)
