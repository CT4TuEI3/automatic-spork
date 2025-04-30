import pandas as pd
import matplotlib.pyplot as plt

path = "/Users/CT4TuEI3/Desktop/Учёба/МДК.01.01 Разработка программных модулей/Git/Seminar5/Titanic.csv"

## 1. Загрузка базы данных из файла Titanic.csv
df = pd.read_csv(path)

## 2. Загрузка базы данных с PassengerId в качестве индекса
dfWithIndex = pd.read_csv(path, index_col="PassengerId")

## 3. Удаление строк с пропущенными значениями
df.dropna(inplace=True)

# Описание базы данных
## 3. Сводная информация о базе данных
print("Сводная информация о данных:")
print(df.info())

## 4. Описательные статистики для количественных показателей
print("\nОписательные статистики:")
print(df.describe())

## 5. Гистограмма для переменной Age
plt.figure(figsize=(10, 6))
plt.hist(df["Age"], color="red", bins=20)
plt.xlabel("Возраст")
plt.ylabel("Количество пассажиров")
plt.title("Распределение возраста пассажиров Титаника")
plt.show()

## 6. Описательные статистики для столбца Fare
print("\nСтатистики для стоимости билета (Fare):")
print(df["Fare"].describe())

# Работа со строками и столбцами базы
## 7. Названия столбцов в виде списка
columnsList = list(df.columns)
print("\nСписок столбцов:", columnsList)

## 8. Переименование столбца Pclass в Class
df.rename(columns={"Pclass": "Class"}, inplace=True)

## 9. Пассажиры женского пола
female = df[df["Sex"] == "female"]

## 10. Выжившие пассажиры мужского пола младше 32 лет
Ymale = df[(df["Survived"] == 1) & (df["Sex"] == "male") & (df["Age"] < 32)]

## 11. Пассажиры 1 или 2 класса
class1Or2 = df[df["Class"].isin([1, 2])]

## 12. Выжившие пассажиры 1 или 2 класса
survivedClass1Or2 = df[(df["Survived"] == 1) & df["Class"].isin([1, 2])]

## 13. Добавление столбца Female (1 - женский пол, 0 - мужской)
df["Female"] = df["Sex"].apply(lambda x: 1 if x == "female" else 0)

# Группировка
## 1. Уникальные значения в столбце Embarked
uniqueEmbarked = df["Embarked"].unique()
print("\nУникальные значения портов посадки:", uniqueEmbarked)

## 2. Группировка по Survived с средними значениями только числовых переменных
# Выбираем только числовые столбцы для расчета среднего
numericCols = df.select_dtypes(include=['int64', 'float64']).columns
survivedGroup = df[numericCols].groupby("Survived").mean()
print("\nСредние значения по числовым переменным в группах выживших:")
print(survivedGroup)

## 3. Группировка по Sex с средними и медианными значениями переменной Age
ageStatsBySex = df.groupby("Sex")["Age"].agg(["mean", "median"])
print("\nСтатистики возраста по полу:")
print(ageStatsBySex)

# Выгрузка базы в файл
## 1. Приведение названий столбцов к нижнему регистру
df.columns = df.columns.str.lower()

## 2. Выгрузка датафрейма в файл Titanic-new.csv
df.to_csv("Titanic-new.csv", index=False)
print("\nДанные успешно сохранены в файл Titanic-new.csv")
