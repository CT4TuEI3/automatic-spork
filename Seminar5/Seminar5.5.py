def createNameAgeDict(names, ages):
    if len(names) != len(ages):
        print("Списки имеют разную длину")
        return {}
    return dict(zip(names, ages))

names = ["Ann", "Tim", "Sam"]
ages = [12, 23, 17]
result = createNameAgeDict(names, ages)
print(result)
